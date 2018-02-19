from .user import Student, Teacher, Admin, Class
from .question import Choice, Page, Judge, Subject, Paper,Record

table_dict = {'student': Student, 'teacher': Teacher, 'admin': Admin,
              'choice': Choice, 'judge': Judge, 'sub': Subject}
