class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary  # lewat setter, jadi langsung divalidasi

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Gaji tidak boleh negatif!")
        self.__salary = value


class Company:
    def __init__(self, name):
        self.name = name
        self.__employees = []  # private: hanya diakses dari dalam class

    def add_employee(self, employee):
        # Validasi tipe sebelum masuk ke list
        if not isinstance(employee, Employee):
            raise TypeError("Hanya objek Employee yang boleh ditambahkan!")
        self.__employees.append(employee)

    def __calculate_payroll(self):
        # Private method: hanya dipanggil dari dalam class
        return sum(e.salary for e in self.__employees)

    def show_payroll(self):
        # Pintu resmi (public) untuk memakai method private
        total = self.__calculate_payroll()
        print(f"Total payroll {self.name}: Rp{total:,}")


if __name__ == "__main__":
    c = Company("Mattel")
    c.add_employee(Employee("Noval", 5_000_000))
    c.add_employee(Employee("Sari", 6_500_000))
    c.show_payroll()

    try:
        c.add_employee("bukan karyawan")
    except TypeError as e:
        print(f"Error: {e}")

    try:
        c.__calculate_payroll()
    except AttributeError as e:
        print(f"Error: {e}")