import os
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, abort, send_file
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import database as db

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'svidetelstva-secret-2026')

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Најавете се за да продолжите.'


@login_manager.user_loader
def load_user(user_id):
    return db.get_user_by_id(user_id)


def admin_required(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            abort(403)
        return f(*args, **kwargs)
    return decorated


# --- Auth ---

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        user = db.authenticate_user(request.form['username'], request.form['password'])
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Невалидно корисничко име или лозинка.', 'error')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


# --- Dashboard ---

@app.route('/')
@login_required
def dashboard():
    classes = db.get_user_classes(current_user.id, current_user.role)
    recent = db.get_certificates(current_user.id, current_user.role)[:10]
    stats = db.get_stats() if current_user.role == 'admin' else None
    return render_template('dashboard.html', classes=classes, recent=recent, stats=stats)


# --- Certificates ---

@app.route('/certificates')
@login_required
def certificates_list():
    class_filter = request.args.get('class_id', '')
    status_filter = request.args.get('status', 'all')
    certs = db.get_certificates(
        current_user.id, current_user.role,
        class_filter or None, status_filter
    )
    classes = db.get_user_classes(current_user.id, current_user.role)
    return render_template('certificates_list.html',
        certificates=certs, classes=classes,
        class_filter=class_filter, status_filter=status_filter)


@app.route('/certificate/new', methods=['GET', 'POST'])
@login_required
def certificate_new():
    if request.method == 'POST':
        cert_id = db.save_certificate(request.form, current_user.id)
        flash('Сведителството е зачувано.', 'success')
        return redirect(url_for('certificate_edit', cert_id=cert_id))
    return render_template('certificate_form.html',
        cert=None,
        classes=db.get_user_classes(current_user.id, current_user.role),
        subjects=db.get_all_subjects(),
        behaviors=db.get_behavior_types(),
        countries=db.get_countries(),
        mk_cities=db.get_mk_cities(),
        settings=db.get_settings(),
        ministries=db.get_all_ministries())


@app.route('/certificate/<int:cert_id>/edit', methods=['GET', 'POST'])
@login_required
def certificate_edit(cert_id):
    cert = db.get_certificate(cert_id)
    if not cert:
        abort(404)
    if request.method == 'POST':
        db.update_certificate(cert_id, request.form)
        flash('Сведителството е ажурирано.', 'success')
        return redirect(url_for('certificate_edit', cert_id=cert_id))
    return render_template('certificate_form.html',
        cert=cert,
        classes=db.get_user_classes(current_user.id, current_user.role),
        subjects=db.get_all_subjects(),
        behaviors=db.get_behavior_types(),
        countries=db.get_countries(),
        mk_cities=db.get_mk_cities(),
        settings=db.get_settings(),
        ministries=db.get_all_ministries())


@app.route('/certificate/<int:cert_id>/print')
@login_required
def certificate_print(cert_id):
    cert = db.get_certificate(cert_id)
    if not cert:
        abort(404)
    settings = db.get_settings()
    return render_template('print_preview.html', cert=cert, settings=settings)


@app.route('/certificate/<int:cert_id>/delete', methods=['POST'])
@login_required
@admin_required
def certificate_delete(cert_id):
    db.delete_certificate(cert_id)
    flash('Сведителството е избришано.', 'success')
    return redirect(url_for('certificates_list'))


# --- API ---

@app.route('/api/students/<int:class_id>')
@login_required
def api_students(class_id):
    return jsonify(db.get_students_by_class(class_id))


@app.route('/api/student/<int:student_id>')
@login_required
def api_student(student_id):
    return jsonify(db.get_student(student_id))


# --- Admin ---

@app.route('/admin')
@login_required
@admin_required
def admin_dashboard():
    return render_template('admin/dashboard.html', stats=db.get_stats())


@app.route('/admin/students', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_students():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            db.add_student(request.form)
            flash('Ученикот е додаден.', 'success')
        elif action == 'edit':
            db.update_student(request.form.get('student_id'), request.form)
            flash('Ученикот е ажуриран.', 'success')
        elif action == 'delete':
            db.delete_student(request.form.get('student_id'))
            flash('Ученикот е избришан.', 'success')
        return redirect(url_for('admin_students'))
    return render_template('admin/students.html',
        students=db.get_all_students(),
        classes=db.get_all_classes(),
        countries=db.get_countries(),
        mk_cities=db.get_mk_cities())


@app.route('/admin/students/clear', methods=['POST'])
@login_required
@admin_required
def admin_students_clear():
    db.clear_students()
    flash('Сите ученици се избришани.', 'success')
    return redirect(url_for('admin_students'))


@app.route('/admin/students/export')
@login_required
@admin_required
def admin_students_export():
    buf = db.export_students_xlsx()
    return send_file(buf, as_attachment=True,
                     download_name='uchenici.xlsx',
                     mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


@app.route('/admin/students/import', methods=['POST'])
@login_required
@admin_required
def admin_students_import():
    f = request.files.get('import_file')
    if not f or not f.filename.endswith('.xlsx'):
        flash('Изберете .xlsx датотека.', 'error')
        return redirect(url_for('admin_students'))
    imported, skipped, unmatched, _, _ = db.import_students_xlsx(f.stream)
    msg = f'Увезени {imported} ученици.'
    if skipped:
        msg += f' Прескокнати {skipped} редови (без ime/презиме).'
    flash(msg, 'success')
    if unmatched:
        flash(f'Непознати паралелки: {", ".join(unmatched)}', 'error')
    return redirect(url_for('admin_students'))


@app.route('/admin/subjects', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_subjects():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            db.add_subject(request.form)
            flash('Предметот е додаден.', 'success')
        elif action == 'delete':
            db.delete_subject(request.form.get('subject_id'))
            flash('Предметот е избришан.', 'success')
        return redirect(url_for('admin_subjects'))
    return render_template('admin/subjects.html', subjects=db.get_all_subjects())


@app.route('/admin/classes', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_classes():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            db.add_class(request.form.get('name'))
            flash('Паралелката е додадена.', 'success')
        elif action == 'delete':
            db.delete_class(request.form.get('class_id'))
            flash('Паралелката е избришана.', 'success')
        return redirect(url_for('admin_classes'))
    return render_template('admin/classes.html', classes=db.get_all_classes())


@app.route('/admin/users', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_users():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            db.add_user(request.form)
            flash('Корисникот е додаден.', 'success')
        elif action == 'delete':
            db.delete_user(request.form.get('user_id'))
            flash('Корисникот е избришан.', 'success')
        elif action == 'change_password':
            db.change_password(request.form.get('user_id'), request.form.get('new_password'))
            flash('Лозинката е променета.', 'success')
        elif action == 'assign_class':
            db.assign_class_to_user(request.form.get('user_id'), request.form.get('class_id'))
        elif action == 'remove_class':
            db.remove_class_from_user(request.form.get('user_id'), request.form.get('class_id'))
        return redirect(url_for('admin_users'))
    return render_template('admin/users.html',
        users=db.get_all_users(),
        classes=db.get_all_classes())


@app.route('/admin/settings', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_settings():
    if request.method == 'POST':
        db.save_settings(request.form)
        flash('Поставките се зачувани.', 'success')
        return redirect(url_for('admin_settings'))
    return render_template('admin/settings.html', settings=db.get_settings(), mk_cities=db.get_mk_cities())


@app.route('/admin/ministries', methods=['GET', 'POST'])
@login_required
@admin_required
def admin_ministries():
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            db.add_ministry(request.form)
            flash('Министерството е додадено.', 'success')
        elif action == 'delete':
            db.delete_ministry(request.form.get('ministry_id'))
            flash('Министерството е избришано.', 'success')
        return redirect(url_for('admin_ministries'))
    return render_template('admin/ministries.html', ministries=db.get_all_ministries())


@app.errorhandler(403)
def forbidden(e):
    return render_template('error.html', code=403, message='Немате пристап до оваа страна.'), 403


@app.errorhandler(404)
def not_found(e):
    return render_template('error.html', code=404, message='Страната не е пронајдена.'), 404


if __name__ == '__main__':
    db.init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
