from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Kết nối đến cơ sở dữ liệu SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=MSI;"
    "DATABASE=QuanLySinhVien;"
    "UID=sa;"
    "PWD=123"
)
cursor = conn.cursor()


# Get data
@app.route("/")
def get_data():
    # Khởi tạo các danh sách rỗng để lưu trữ CSDL
    sinh_vien_info = []
    mon_hoc_info = []
    diem_info = []
    giang_vien_info = []
    lop_hoc_info = []
    khoa_info = []
    nganh_info = []
    dang_ky_info = []
    phu_trach_info = []

    # Lấy danh sách sinh viên từ CSDL
    query = "SELECT * FROM Sinh_Vien"
    cursor.execute(query)
    sinh_vien_info = [row for row in cursor.fetchall()]

    # Lấy danh sách môn học từ CSDL
    query = "SELECT * FROM Mon_Hoc"
    cursor.execute(query)
    mon_hoc_info = [row for row in cursor.fetchall()]

    # Lấy danh sách điểm từ CSDL
    query = "SELECT * FROM Diem"
    cursor.execute(query)
    diem_info = [row for row in cursor.fetchall()]

    # Lấy danh sách giảng viên từ CSDL
    query = "SELECT * FROM Giang_Vien"
    cursor.execute(query)
    giang_vien_info = [row for row in cursor.fetchall()]

    # Lấy danh sách lớp học từ CSDL
    query = "SELECT * FROM Lop_Hoc"
    cursor.execute(query)
    lop_hoc_info = [row for row in cursor.fetchall()]

    # Lấy danh sách khoa từ CSDL
    query = "SELECT * FROM Khoa"
    cursor.execute(query)
    khoa_info = [row for row in cursor.fetchall()]

    # Lấy danh sách ngành từ CSDL
    query = "SELECT * FROM Nganh"
    cursor.execute(query)
    nganh_info = [row for row in cursor.fetchall()]

    # Lấy danh sách đăng ký từ CSDL
    query = "SELECT * FROM Dang_Ky"
    cursor.execute(query)
    dang_ky_info = [row for row in cursor.fetchall()]

    # Lấy danh sách phụ trách từ CSDL
    query = "SELECT * FROM Phu_Trach"
    cursor.execute(query)
    phu_trach_info = [row for row in cursor.fetchall()]

    return render_template(
        "index.html",
        sinh_vien_info=sinh_vien_info,
        mon_hoc_info=mon_hoc_info,
        diem_info=diem_info,
        giang_vien_info=giang_vien_info,
        lop_hoc_info=lop_hoc_info,
        khoa_info=khoa_info,
        nganh_info=nganh_info,
        dang_ky_info=dang_ky_info,
        phu_trach_info=phu_trach_info,
    )


# Thêm sinh viên
@app.route("/add_sinh_vien", methods=["POST"])
def add_sinh_vien():
    ma_sv = request.form["ma_sv"]
    ho_ten = request.form["ho_ten"]
    ngay_sinh = request.form["ngay_sinh"]
    gioi_tinh = request.form["gioi_tinh"]
    noi_sinh = request.form["noi_sinh"]
    so_dien_thoai = request.form["so_dien_thoai"]
    email = request.form["email"]
    ma_khoa = request.form["ma_khoa"]
    ma_nganh = request.form["ma_nganh"]

    query = "INSERT INTO Sinh_Vien (Ma_SV, Ho_Ten, Ngay_Sinh, Gioi_Tinh, Noi_Sinh, So_Dien_Thoai, Email, Ma_Khoa, Ma_Nganh) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = (
        ma_sv,
        ho_ten,
        ngay_sinh,
        gioi_tinh,
        noi_sinh,
        so_dien_thoai,
        email,
        ma_khoa,
        ma_nganh,
    )
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Sửa sinh viên
@app.route("/update_sinh_vien", methods=["POST"])
def update_sinh_vien():
    ma_sv = request.form["ma_sv"]
    ho_ten = request.form["ho_ten"]
    ngay_sinh = request.form["ngay_sinh"]
    gioi_tinh = request.form["gioi_tinh"]
    noi_sinh = request.form["noi_sinh"]
    so_dien_thoai = request.form["so_dien_thoai"]
    email = request.form["email"]
    ma_khoa = request.form["ma_khoa"]
    ma_nganh = request.form["ma_nganh"]

    query = "UPDATE Sinh_Vien SET Ho_Ten = ?, Ngay_Sinh = ?, Gioi_Tinh = ?, Noi_Sinh = ?, So_Dien_Thoai = ?, Email = ?, Ma_Khoa = ?, Ma_Nganh = ? WHERE Ma_SV = ?"
    values = (
        ho_ten,
        ngay_sinh,
        gioi_tinh,
        noi_sinh,
        so_dien_thoai,
        email,
        ma_khoa,
        ma_nganh,
        ma_sv,
    )
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Xóa sinh viên
@app.route("/delete_sinh_vien/<ma_sv>", methods=["POST"])
def delete_sinh_vien(ma_sv):
    query = "DELETE FROM Sinh_Vien WHERE ma_sv = ?"
    values = (ma_sv,)
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))
    query = "SELECT COUNT(*) FROM Sinh_Vien WHERE ma_sv = ?"
    cursor.execute(query, (ma_sv,))
    count = cursor.fetchone()[0]
    return count > 0


# Thêm môn học
@app.route("/add_mon_hoc", methods=["POST"])
def add_mon_hoc():
    ma_mon = request.form["ma_mon"]
    ten_mon = request.form["ten_mon"]
    so_tin_chi = request.form["so_tin_chi"]
    ma_lop = request.form["ma_lop"]

    query = (
        "INSERT INTO Mon_Hoc (Ma_Mon, Ten_Mon, So_Tin_Chi, Ma_Lop) VALUES (?, ?, ?, ?)"
    )
    values = (ma_mon, ten_mon, so_tin_chi, ma_lop)
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Sửa môn học
@app.route("/update_mon_hoc", methods=["POST"])
def update_mon_hoc():
    ma_mon = request.form["ma_mon"]
    ten_mon = request.form["ten_mon"]
    so_tin_chi = request.form["so_tin_chi"]
    ma_lop = request.form["ma_lop"]

    query = "UPDATE Mon_Hoc SET Ma_Mon = ?, Ten_Mon = ?, So_Tin_Chi = ?, Ma_Lop = ? WHERE Ma_Mon = ?"

    values = (ma_mon, ten_mon, so_tin_chi, ma_lop)
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Xóa môn học
@app.route("/delete_mon_hoc/<ma_mon>", methods=["POST"])
def delete_mon_hoc(ma_mon):
    query = "DELETE FROM Mon_Hoc WHERE ma_mon = ?"
    values = (ma_mon,)
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Thêm điểm
@app.route("/add_diem", methods=["POST"])
def add_diem():
    ma_diem = request.form["ma_diem"]
    diem_bt = request.form["diem_bt"]
    diem_gk = request.form["diem_gk"]
    diem_ck = request.form["diem_ck"]
    diem_tk = request.form["diem_tk"]
    ket_qua = request.form["ket_qua"]
    ma_sv = request.form["ma_sv"]
    ma_mon = request.form["ma_mon"]

    query = "INSERT INTO Diem (Ma_Diem, Diem_Bt, Diem_Gk, Diem_Ck, Diem_Tk, Ket_qua, Ma_Sv, Ma_Mon) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
    values = (ma_diem, diem_bt, diem_gk, diem_ck, diem_tk, ket_qua, ma_sv, ma_mon)
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Sửa điểm
@app.route("/update_diem", methods=["POST"])
def update_diem():
    ma_diem = request.form["ma_diem"]
    diem_bt = request.form["diem_bt"]
    diem_gk = request.form["diem_gk"]
    diem_ck = request.form["diem_ck"]
    diem_tk = request.form["diem_tk"]
    ket_qua = request.form["ket_qua"]
    ma_sv = request.form["ma_sv"]
    ma_mon = request.form["ma_mon"]

    query = "UPDATE Diem SET ma_diem = ?, diem_bt = ?, diem_gk = ?, diem_ck = ?, diem_tk = ?, ket_qua = ?, ma_sv = ?, ma_mon = ? WHERE ma_diem = ?"

    values = (ma_diem, diem_bt, diem_gk, diem_ck, diem_tk, ket_qua, ma_sv, ma_mon)
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Xóa điểm
@app.route("/delete_diem/<ma_diem>", methods=["POST"])
def delete_diem(ma_diem):
    query = "DELETE FROM Diem WHERE ma_diem = ?"
    values = (ma_diem,)
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Thêm giảng viên
@app.route("/add_giang_vien", methods=["POST"])
def add_giang_vien():
    ma_gv = request.form["ma_gv"]
    ho_ten = request.form["ho_ten"]
    ngay_sinh = request.form["ngay_sinh"]
    gioi_tinh = request.form["gioi_tinh"]
    so_dien_thoai = request.form["so_dien_thoai"]
    email = request.form["email"]

    query = "INSERT INTO Giang_Vien (Ma_GV, Ho_Ten, Ngay_Sinh, Gioi_Tinh, So_Dien_Thoai, Email) VALUES (?, ?, ?, ?, ?, ?)"
    values = (
        ma_gv,
        ho_ten,
        ngay_sinh,
        gioi_tinh,
        so_dien_thoai,
        email,
    )
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Sửa giảng viên
@app.route("/update_giang_vien", methods=["POST"])
def update_giang_vien():
    ma_gv = request.form["ma_gv"]
    ho_ten = request.form["ho_ten"]
    ngay_sinh = request.form["ngay_sinh"]
    gioi_tinh = request.form["gioi_tinh"]
    so_dien_thoai = request.form["so_dien_thoai"]
    email = request.form["email"]

    query = "UPDATE Giang_Vien SET ma_gv = ?, ho_ten = ?, ngay_sinh = ?, gioi_tinh = ?, so_dien_thoai = ?, email = ?"
    values = (
        ma_gv,
        ho_ten,
        ngay_sinh,
        gioi_tinh,
        so_dien_thoai,
        email,
    )
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Xóa giảng viên
@app.route("/delete_giang_vien/<ma_gv>", methods=["POST"])
def delete_giang_vien(ma_gv):
    query = "DELETE FROM Giang_Vien WHERE ma_gv = ?"
    values = (ma_gv,)
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Thêm lớp học
@app.route("/add_lop_hoc", methods=["POST"])
def add_lop_hoc():
    ma_lop = request.form["ma_lop"]
    phong_hoc = request.form["phong_hoc"]

    query = "INSERT INTO Lop_Hoc (Ma_Lop, Phong_Hoc) VALUES (?, ?)"
    values = (
        ma_lop,
        phong_hoc,
    )
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Sửa lớp học
@app.route("/update_lop_hoc", methods=["POST"])
def update_lop_hoc():
    ma_lop = request.form["ma_lop"]
    phong_hoc = request.form["phong_hoc"]

    query = "UPDATE Lop_Hoc SET ma_lop = ?, phong_hoc = ?"
    values = (
        ma_lop,
        phong_hoc,
    )
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))

# Xóa lớp học
@app.route("/delete_lop_hoc/<ma_lop>", methods=["POST"])
def delete_lop_hoc(ma_lop):
    query = "DELETE FROM Lop_Hoc WHERE ma_lop = ?"
    values = (ma_lop,)
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Thêm khoa
@app.route("/add_khoa", methods=["POST"])
def add_khoa():
    ma_khoa = request.form["ma_khoa"]
    ten_khoa = request.form["ten_khoa"]

    query = "INSERT INTO Khoa (ma_khoa, ten_khoa) VALUES (?, ?)"
    values = (
        ma_khoa,
        ten_khoa,
    )
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Sửa khoa
@app.route("/update_khoa", methods=["POST"])
def update_khoa():
    ma_khoa = request.form["ma_khoa"]
    ten_khoa = request.form["ten_khoa"]

    query = "UPDATE Khoa SET ma_khoa = ?, ten_khoa = ?"
    values = (
        ma_khoa,
        ten_khoa,
    )
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))

# Xóa khoa
@app.route("/delete_khoa/<ma_khoa>", methods=["POST"])
def delete_khoa(ma_khoa):
    query = "DELETE FROM Khoa WHERE ma_khoa = ?"
    values = (ma_khoa,)
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Thêm ngành
@app.route("/add_nganh", methods=["POST"])
def add_nganh():
    ma_nganh = request.form["ma_nganh"]
    ten_nganh = request.form["ten_nganh"]

    query = "INSERT INTO Nganh (ma_nganh, ten_nganh) VALUES (?, ?)"
    values = (
        ma_nganh,
        ten_nganh,
    )
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))


# Sửa ngành
@app.route("/update_nganh", methods=["POST"])
def update_nganh():
    ma_nganh = request.form["ma_nganh"]
    ten_nganh = request.form["ten_nganh"]

    query = "UPDATE Khoa SET ma_nganh = ?, ten_nganh = ?"
    values = (
        ma_nganh,
        ten_nganh,
    )
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))

# Xóa ngành
@app.route("/delete_nganh/<ma_nganh>", methods=["POST"])
def delete_nganh(ma_nganh):
    query = "DELETE FROM Nganh WHERE ma_nganh = ?"
    values = (ma_nganh,)
    cursor.execute(query, values)
    conn.commit()
    return redirect(url_for("get_data"))

if __name__ == "__main__":
    app.run()
