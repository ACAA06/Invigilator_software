from django.test import TestCase
from software.models import *
from django.contrib.auth.models import User

class DepartmentTestCase(TestCase):
    def setUp(self):
        Department.objects.create(did=1, dname="some_dept")
        Department.objects.create(did=3, dname="unknown_dept")

    def test_dept(self):
        """Check if departments are identified"""
        test1 = Department.objects.get(did=1)
        test2 = Department.objects.get(did=3)
        self.assertEqual(test1.dname, 'some_dept')
        self.assertEqual(test2.dname, 'unknown_dept')

class FDetailTestCase(TestCase):
    def setUp(self):
        lol=User(username="username", password="password")
        lol.save()
        Department.objects.create(did=1, dname="some_dept")
        fdetail.objects.create(fid=lol, countofduties=5, timetable="ftimetable\\fac1 - Sheet1 (1)_4x4sSLy.csv", did=Department(did=1, dname="some_dept"))

    def test_fdetail(self):
        """Check if FDetails are identified"""
        lol=User(username="username", password="password")
        test1 = fdetail.objects.get(countofduties=5)
        self.assertEqual(test1.countofduties, 5)

class ExamTestCase(TestCase):
    def setUp(self):
        Exam.objects.create(eid=1, etimetable="ftimetable/final-exam-tt - Sheet1 (2)_AY3kUlc.csv", year=2020, allot=False, students=30)

    def test_exam(self):
        """Check if Exam is identified"""
        test1 = Exam.objects.get(eid=1)
        self.assertEqual(test1.year, 2020)

class SubjectTestCase(TestCase):
    def setUp(self):
        Subject.objects.create(sname="test_case", scode=1)

    def test_subject(self):
        """Subjects are correctly identified"""
        test1 = Subject.objects.get(scode=1)
        self.assertEqual(test1.sname, "test_case")

class StrengthTestCase(TestCase):
    def setUp(self):
        Department.objects.create(did=1, dname="some_dept")
        Strength.objects.create(department=Department(did=1, dname="some_dept"),year=2020, strength=60)

    def test_strength(self):
        """Strength is correctly identified"""
        test1 = Strength.objects.get(year=2020)
        self.assertEqual(test1.strength, 60)

class BuildingTestCase(TestCase):
    def setUp(self):
        Department.objects.create(did=1, dname="some_dept")
        Building.objects.create(department=Department(did=1, dname="some_dept"),buildingname="AB3")

    def test_building(self):
        """Buildings are correctly identified"""
        test1 = Building.objects.get(buildingname="AB3")
        self.assertEqual(test1.buildingname, "AB3")

class RoomTestCase(TestCase):
    def setUp(self):
        Department.objects.create(did=1, dname="some_dept")
        Building.objects.create(department=Department(did=1, dname="some_dept"),buildingname="AB3")
        kek=Building(department=Department(did=1, dname="some_dept"),buildingname="AB3")
        kek.save()
        Rooms.objects.create(roomno="G303", building=kek, roomtt="ftimetable/A102.csv", strength=30)

    def test_rooms(self):
        """Rooms are correctly identified"""
        test1 = Rooms.objects.get(roomno="G303")
        self.assertEqual(test1.roomno,"G303")

class AllotmentTestCase(TestCase):
    def setUp(self):
        lol=User(username="username", password="password")
        lol.save()
        Department.objects.create(did=1, dname="some_dept")
        Building.objects.create(department=Department(did=1, dname="some_dept"),buildingname="AB3")
        kek=Building(department=Department(did=1, dname="some_dept"),buildingname="AB3")
        kek.save()
        Rooms.objects.create(roomno="G303", building=kek)
        lel=Rooms(roomno="G303", building=kek)
        lel.save()         
        allotment.objects.create(fid=lol, date="1/1/2020", time="9:30", ename="K0", semester="S7", sname="MOT", roomno=lel, alter=False)
        
    def test_allotment(self):
        """Allotments are correctly identified"""
        test1 = allotment.objects.get(ename="K0")
        self.assertEqual(test1.semester, "S7")

class AvailableTestCase(TestCase):
    def setUp(self):
        lol=User(username="username", password="password")
        lol.save()
        Available.objects.create(fid=lol, date="1/1/2020", Time="9:30")

    def test_available(self):
        """Availables are correctly identified"""
        test1 = Available.objects.get(date="1/1/2020")
        self.assertEqual(test1.time,"9:30")