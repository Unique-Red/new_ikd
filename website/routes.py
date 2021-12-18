from flask import render_template, session, request, redirect, url_for, flash, Blueprint
from sqlalchemy.sql.functions import current_user
from .models import Post, User
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from website import app, db
import os


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


@app.route("/")
def welcome():
    return render_template ("welcome.html")
    
@app.route("/home")
def home():
    posts = Post.query.order_by(Post.date_created.desc()).all()
    return render_template ("home.html", posts=posts)

@app.route("/legislative")
def legislative():
    posts = Post.query.all()
    return render_template ("legislatives.html", posts=posts)

@app.route("/executive")
def executive():
    posts = Post.query.all()
    return render_template ("executive.html", posts=posts)

@app.route("/political")
def political():
    posts = Post.query.all()
    return render_template ("political.html", posts=posts)

@app.route("/traditional")
def traditional():
    posts = Post.query.all()
    return render_template ("traditional.html", posts=posts)

@app.route("/nulge")
def nulge():
    posts = Post.query.all()
    return render_template ("nulge.html", posts=posts)

@app.route("/past-leaders")
def past():
    posts = Post.query.all()
    return render_template ("past.html", posts=posts)

@app.route("/heritage")
def heritage():
    posts = Post.query.all()
    return render_template ("heritage.html", posts=posts)


@app.route("/historical")
def historical():
    posts = Post.query.all()
    return render_template ("history.html", posts=posts)


@app.route("/political-leader")
def pol():
    posts = Post.query.all()
    return render_template ("pol.html", posts=posts)

@app.route("/sons&daughters")
def s_d():
    posts = Post.query.all()
    return render_template ("s&d.html", posts=posts)

@app.route("/judiciary")
def judiciary():
    posts = Post.query.all()
    return render_template ("judiciary.html", posts=posts)

@app.route("/administrative")
def administrative():
    posts = Post.query.all()
    return render_template ("administrative.html", posts=posts)

@app.route("/image")
def image():
    posts = Post.query.order_by(Post.date_created.desc()).all()
    return render_template ("images.html", posts=posts)

@app.route("/contact")
def contact():
    posts = Post.query.all()
    return render_template ("contactt.html", posts=posts)

@app.route("/project")
def project():
    posts = Post.query.order_by(Post.date_created.desc()).all()
    return render_template ("project.html", posts=posts)

@app.route("/post/<int:id>")
def post(id):
    post = Post.query.get_or_404(id)
    return render_template ("post.html", post=post)

@app.route("/auth", methods=["GET", "POST"])
def auth():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                login_user(user, remember=True)
                return redirect(url_for('table'))
            else:
                flash("Password is incorrect", category='error') 
        else:
            flash("Username does not exist", category='error')

    return render_template ("admin/auth.html")


@app.route("/reg", methods=["GET", "POST"])
def reg():
    if request.method == "POST":
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        username_exists = User.query.filter_by(username=username).first()
        if username_exists:
            flash("Username in use.", category='error') 
        elif password1 != password2:
            flash("Password don't match!", category='error') 
        elif len(username) < 2:
            flash("Username is too short", category='error') 
        elif len(password1) < 6:
            flash("Password is too short", category='error')
        else:
            new_user = User(username=username, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('table'))


    return render_template ("admin/register.html")
    

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/home")

@app.route("/create", methods=['GET', 'POST'])
@login_required
def create():
    if request.method == "POST":
            title = request.form.get("title")
            stext = request.form.get("stext")
            text = request.form.get("text")
            file = request.files.get("file")
            file1 = request.files.get("file1")
            file2 = request.files.get("file2")
            file3 = request.files.get("file3")
            file4 = request.files.get("file4")
            file5 = request.files.get("file5")
            file6 = request.files.get("file6")
            file7 = request.files.get("file7")
            file8 = request.files.get("file8")
            file9 = request.files.get("file9")
            file10 = request.files.get("file10")
            file11 = request.files.get("file11")
            file12 = request.files.get("file12")
            file13 = request.files.get("file13")
            file14 = request.files.get("file14")

            if not text:
                return ('Details cannot be empty!')
            else:
                path = os.path.join("website", "static", "uploads", file.filename)
                path1 = os.path.join("website", "static", "uploads", file1.filename)
                path2 = os.path.join("website", "static", "uploads", file2.filename)
                path3 = os.path.join("website", "static", "uploads", file3.filename)
                path4 = os.path.join("website", "static", "uploads", file4.filename)
                path5 = os.path.join("website", "static", "uploads", file5.filename)
                path6 = os.path.join("website", "static", "uploads", file6.filename)
                path7 = os.path.join("website", "static", "uploads", file7.filename)
                path8 = os.path.join("website", "static", "uploads", file8.filename)
                path9 = os.path.join("website", "static", "uploads", file9.filename)
                path10 = os.path.join("website", "static", "uploads", file10.filename)
                path11 = os.path.join("website", "static", "uploads", file11.filename)
                path12 = os.path.join("website", "static", "uploads", file12.filename)
                path13 = os.path.join("website", "static", "uploads", file13.filename)
                path14 = os.path.join("website", "static", "uploads", file14.filename)
                post = Post(title=title, stext=stext, text=text, file=file.filename, file1=file1.filename, file2=file2.filename, file3=file3.filename, file4=file4.filename, file5=file5.filename, file6=file6.filename, file7=file7.filename, file8=file8.filename, file9=file9.filename, file10=file10.filename, file11=file11.filename, file12=file12.filename, file13=file13.filename, file14=file14.filename,)
                file.save(path)
                file1.save(path1)
                file2.save(path2)
                file3.save(path3)
                file4.save(path4)
                file5.save(path5)
                file6.save(path6)
                file7.save(path7)
                file8.save(path8)
                file9.save(path9)
                file10.save(path10)
                file11.save(path11)
                file12.save(path12)
                file13.save(path13)
                file14.save(path14)

                
                db.session.add(post)
                db.session.commit()

                return redirect(url_for('project'))
    return render_template ("admin/create.html")

@app.route("/table", methods=["GET","POST"])
@login_required
def table():
    posts = Post.query.all()
    return render_template ("admin/table.html", posts=posts)

@app.route("/title", methods=["GET","POST"])
@login_required
def title():
    posts = Post.query.all()
    return render_template ("admin/title.html", posts=posts)

@app.route("/text", methods=["GET","POST"])
@login_required
def text():
    posts = Post.query.all()
    return render_template ("admin/text.html", posts=posts)

@app.route("/stext", methods=["GET","POST"])
@login_required
def stext():
    posts = Post.query.all()
    return render_template ("admin/stext.html", posts=posts)



@app.route("/updatetitle/<int:id>", methods=['GET','POST'])
@login_required
def updatetitle(id):
    title_to_update = Post.query.get_or_404(id)
    if request.method=="POST":
        title_to_update.title = request.form['title']
        try:
            db.session.commit()
            return redirect('/title')

        except:
            flash("There was a problem updating this title")
    else:
        return render_template("admin/updatetitle.html", title_to_update=title_to_update)



@app.route("/updatetext/<int:id>", methods=["GET","POST"])
@login_required
def updatetext(id):
    text_to_update = Post.query.get_or_404(id)
    if request.method=="POST":
        text_to_update.text = request.form['text']
        try:
            db.session.commit()
            return redirect('/text')

        except:
            flash("There was a problem updating this project")
    else:
        return render_template("admin/updatetext.html", text_to_update=text_to_update)


@app.route("/updatestext/<int:id>", methods=["GET","POST"])
@login_required
def updatestext(id):
    stext_to_update = Post.query.get_or_404(id)
    if request.method=="POST":
        stext_to_update.stext = request.form['stext']
        try:
            db.session.commit()
            return redirect('/stext')

        except:
            flash("There was a problem updating this project")
    else:
        return render_template("admin/updatestext.html", stext_to_update=stext_to_update)


@app.route("/delete/<int:id>")
@login_required
def delete(id):
    project_delete = Post.query.get_or_404(id)

    try:
        db.session.delete(project_delete)
        db.session.commit()
        return redirect("/table")

    except:
        flash("There was a problem deleting this project", category='error')