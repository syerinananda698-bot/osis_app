from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3, os
from functools import wraps

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "osis.db")

app = Flask(__name__)
app.config["SECRET_KEY"] = "ganti_rahasiamu"
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if not os.path.exists(DB_PATH):
        conn = get_db()
        c = conn.cursor()
        c.execute('''CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )''')
        c.execute('''CREATE TABLE anggota (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            kelas TEXT,
            jabatan TEXT
        )''')
        c.execute('''CREATE TABLE kegiatan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_kegiatan TEXT,
            tanggal TEXT,
            keterangan TEXT
        )''')
        c.execute('''CREATE TABLE surat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomor_surat TEXT,
            perihal TEXT,
            tanggal TEXT
        )''')
        # default admin
        c.execute("INSERT INTO user (username, password) VALUES (?, ?)", ("admin", "admin"))
        conn.commit()
        conn.close()

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            flash("Silakan login terlebih dahulu.", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

@app.route("/")
def welcome():
    return render_template("welcome.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username = request.form.get("username","").strip()
        password = request.form.get("password","")
        conn = get_db()
        cur = conn.execute("SELECT * FROM user WHERE username=? AND password=?", (username, password))
        user = cur.fetchone()
        conn.close()
        if user:
            session["user"] = user["username"]
            flash("Login berhasil.", "success")
            return redirect(url_for("dashboard"))
        flash("Login gagal. Cek username/password.", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("Anda telah logout.", "info")
    return redirect(url_for("welcome"))

@app.route("/dashboard")
@login_required
def dashboard():
    conn = get_db()
    total_anggota = conn.execute("SELECT COUNT(*) AS c FROM anggota").fetchone()["c"]
    total_kegiatan = conn.execute("SELECT COUNT(*) AS c FROM kegiatan").fetchone()["c"]
    total_surat = conn.execute("SELECT COUNT(*) AS c FROM surat").fetchone()["c"]
    conn.close()
    return render_template("dashboard.html", total_anggota=total_anggota, total_kegiatan=total_kegiatan, total_surat=total_surat)

# --- ANGGOTA ---
@app.route("/anggota")
@login_required
def anggota_list():
    conn = get_db()
    items = conn.execute("SELECT * FROM anggota ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("anggota.html", items=items)

@app.route("/anggota/new", methods=["GET","POST"])
@login_required
def anggota_new():
    if request.method=="POST":
        nama = request.form.get("nama","").strip()
        kelas = request.form.get("kelas","").strip()
        jabatan = request.form.get("jabatan","").strip()
        conn = get_db()
        conn.execute("INSERT INTO anggota (nama, kelas, jabatan) VALUES (?, ?, ?)", (nama, kelas, jabatan))
        conn.commit(); conn.close()
        flash("Anggota ditambahkan.", "success")
        return redirect(url_for("anggota_list"))
    return render_template("anggota_form.html", item=None)

@app.route("/anggota/<int:id>/edit", methods=["GET","POST"])
@login_required
def anggota_edit(id):
    conn = get_db()
    item = conn.execute("SELECT * FROM anggota WHERE id=?", (id,)).fetchone()
    if request.method=="POST":
        nama = request.form.get("nama","").strip()
        kelas = request.form.get("kelas","").strip()
        jabatan = request.form.get("jabatan","").strip()
        conn.execute("UPDATE anggota SET nama=?, kelas=?, jabatan=? WHERE id=?", (nama, kelas, jabatan, id))
        conn.commit(); conn.close()
        flash("Anggota diperbarui.", "success")
        return redirect(url_for("anggota_list"))
    conn.close()
    return render_template("anggota_form.html", item=item)

@app.route("/anggota/<int:id>/delete", methods=["POST"])
@login_required
def anggota_delete(id):
    conn = get_db()
    conn.execute("DELETE FROM anggota WHERE id=?", (id,))
    conn.commit(); conn.close()
    flash("Anggota dihapus.", "info")
    return redirect(url_for("anggota_list"))

# --- KEGIATAN ---
@app.route("/kegiatan")
@login_required
def kegiatan_list():
    conn = get_db()
    items = conn.execute("SELECT * FROM kegiatan ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("kegiatan.html", items=items)

@app.route("/kegiatan/new", methods=["GET","POST"])
@login_required
def kegiatan_new():
    if request.method=="POST":
        nama_kegiatan = request.form.get("nama_kegiatan","").strip()
        tanggal = request.form.get("tanggal","").strip()
        keterangan = request.form.get("keterangan","").strip()
        conn = get_db()
        conn.execute("INSERT INTO kegiatan (nama_kegiatan, tanggal, keterangan) VALUES (?, ?, ?)", (nama_kegiatan, tanggal, keterangan))
        conn.commit(); conn.close()
        flash("Kegiatan ditambahkan.", "success")
        return redirect(url_for("kegiatan_list"))
    return render_template("kegiatan_form.html", item=None)

@app.route("/kegiatan/<int:id>/edit", methods=["GET","POST"])
@login_required
def kegiatan_edit(id):
    conn = get_db()
    item = conn.execute("SELECT * FROM kegiatan WHERE id=?", (id,)).fetchone()
    if request.method=="POST":
        nama_kegiatan = request.form.get("nama_kegiatan","").strip()
        tanggal = request.form.get("tanggal","").strip()
        keterangan = request.form.get("keterangan","").strip()
        conn.execute("UPDATE kegiatan SET nama_kegiatan=?, tanggal=?, keterangan=? WHERE id=?", (nama_kegiatan, tanggal, keterangan, id))
        conn.commit(); conn.close()
        flash("Kegiatan diperbarui.", "success")
        return redirect(url_for("kegiatan_list"))
    conn.close()
    return render_template("kegiatan_form.html", item=item)

@app.route("/kegiatan/<int:id>/delete", methods=["POST"])
@login_required
def kegiatan_delete(id):
    conn = get_db()
    conn.execute("DELETE FROM kegiatan WHERE id=?", (id,))
    conn.commit(); conn.close()
    flash("Kegiatan dihapus.", "info")
    return redirect(url_for("kegiatan_list"))

# --- SURAT ---
@app.route("/surat")
@login_required
def surat_list():
    conn = get_db()
    items = conn.execute("SELECT * FROM surat ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("surat.html", items=items)

@app.route("/surat/new", methods=["GET","POST"])
@login_required
def surat_new():
    if request.method=="POST":
        nomor_surat = request.form.get("nomor_surat","").strip()
        perihal = request.form.get("perihal","").strip()
        tanggal = request.form.get("tanggal","").strip()
        conn = get_db()
        conn.execute("INSERT INTO surat (nomor_surat, perihal, tanggal) VALUES (?, ?, ?)", (nomor_surat, perihal, tanggal))
        conn.commit(); conn.close()
        flash("Surat ditambahkan.", "success")
        return redirect(url_for("surat_list"))
    return render_template("surat_form.html", item=None)

@app.route("/surat/<int:id>/edit", methods=["GET","POST"])
@login_required
def surat_edit(id):
    conn = get_db()
    item = conn.execute("SELECT * FROM surat WHERE id=?", (id,)).fetchone()
    if request.method=="POST":
        nomor_surat = request.form.get("nomor_surat","").strip()
        perihal = request.form.get("perihal","").strip()
        tanggal = request.form.get("tanggal","").strip()
        conn.execute("UPDATE surat SET nomor_surat=?, perihal=?, tanggal=? WHERE id=?", (nomor_surat, perihal, tanggal, id))
        conn.commit(); conn.close()
        flash("Surat diperbarui.", "success")
        return redirect(url_for("surat_list"))
    conn.close()
    return render_template("surat_form.html", item=item)

@app.route("/surat/<int:id>/delete", methods=["POST"])
@login_required
def surat_delete(id):
    conn = get_db()
    conn.execute("DELETE FROM surat WHERE id=?", (id,))
    conn.commit(); conn.close()
    flash("Surat dihapus.", "info")
    return redirect(url_for("surat_list"))

# --- SEARCH ---
@app.route("/search")
@login_required
def search():
    q = request.args.get("q","").strip()
    conn = get_db()
    anggota = conn.execute("SELECT * FROM anggota WHERE nama LIKE ?", ('%'+q+'%',)).fetchall()
    kegiatan = conn.execute("SELECT * FROM kegiatan WHERE nama_kegiatan LIKE ?", ('%'+q+'%',)).fetchall()
    surat = conn.execute("SELECT * FROM surat WHERE perihal LIKE ?", ('%'+q+'%',)).fetchall()
    conn.close()
    return render_template("search.html", anggota=anggota, kegiatan=kegiatan, surat=surat, q=q)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
