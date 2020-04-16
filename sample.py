@main.route('/delete/<int:id>')
def delete(id):
    to_delete = record.query.get_or_404(id)

    try:
        db.session.delete(to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return render_template('Calculator.html')





@main.route('/calculator')
@login_required
def calculator():
    all_data = record.query.filter(record.email == current_user.email)
    return render_template('Calculator.html', email=current_user.email, ALLhistory=all_data)


