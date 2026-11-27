
from SinhVien import SinhVien


class QuanLySinhVien:
    listSinhVien = []

    # Tao ID tu dong
    def generateID(self):
        maxId = 0

        if self.soLuongSinhVien() > 0:
            maxId = max(sv._id for sv in self.listSinhVien)

        return maxId + 1

    # Dem so luong sinh vien
    def soLuongSinhVien(self):
        return len(self.listSinhVien)

    # Nhap sinh vien
    def nhapSinhVien(self):
        svId = self.generateID()

        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh cua sinh vien: ")
        diemTB = float(input("Nhap diem cua sinh vien: "))

        sv = SinhVien(svId, name, sex, major, diemTB)

        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    # Cap nhat thong tin sinh vien
    def updateSinhVien(self, ID):
        sv = self.findByID(ID)

        if sv is not None:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh cua sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))

            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB

            self.xepLoaiHocLuc(sv)

            print("Cap nhat sinh vien thanh cong!")
        else:
            print("Sinh vien co ID = {} khong ton tai.".format(ID))

    # Sap xep theo ID
    def sortByID(self):
        self.listSinhVien.sort(
            key=lambda x: x._id,
            reverse=False
        )

    # Sap xep theo ten
    def sortByName(self):
        self.listSinhVien.sort(
            key=lambda x: x._name.lower(),
            reverse=False
        )

    # Sap xep theo diem trung binh
    def sortByDiemTB(self):
        self.listSinhVien.sort(
            key=lambda x: x._diemTB,
            reverse=False
        )

    # Tim sinh vien theo ID
    def findByID(self, ID):
        searchResult = None

        for sv in self.listSinhVien:
            if sv._id == ID:
                searchResult = sv
                break

        return searchResult

    # Tim sinh vien theo ten
    def findByName(self, keyword):
        listSV = []

        for sv in self.listSinhVien:
            if keyword.upper() in sv._name.upper():
                listSV.append(sv)

        return listSV

    # Xoa sinh vien theo ID
    def deleteById(self, ID):
        sv = self.findByID(ID)

        if sv is not None:
            self.listSinhVien.remove(sv)
            return True

        return False

    # Xep loai hoc luc
    def xepLoaiHocLuc(self, sv):
        if sv._diemTB >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    # Hien thi danh sach sinh vien
    def showSinhVien(self, listSV):
        print(
            "{:<8}{:<18}{:<10}{:<18}{:<10}{:<12}".format(
                "ID", "Name", "Sex", "Major", "Diem TB", "Hoc luc"
            )
        )

        if len(listSV) > 0:
            for sv in listSV:
                print(
                    "{:<8}{:<18}{:<10}{:<18}{:<10}{:<12}".format(
                        sv._id,
                        sv._name,
                        sv._sex,
                        sv._major,
                        sv._diemTB,
                        sv._hocLuc
                    )
                )

        print("\n")

    # Lay danh sach sinh vien
    def getListSinhVien(self):
        return self.listSinhVien
