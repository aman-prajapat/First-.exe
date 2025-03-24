import mysql.connector as mc

empDB = mc.connect(
    host="localhost",  
    port=3306,         
    user="root",
    password="0000",
    database="test"
)

test_cursor = empDB.cursor()

def add(employeeId,empName,mobile,email,post):
    query = "insert into emp (employeeId,empName,mobile,email,post) values (%s,%s,%s,%s,%s)"
    test_cursor.execute(query,(employeeId,empName,mobile,email,post))
    empDB.commit()

def remove(empId):
    query = "delete from emp where employeeId = %s"
    test_cursor.execute(query,(empId,))
    empDB.commit()

def promote(post,empId):
    query = "update emp set post = %s where employeeId = %s"
    test_cursor.execute(query,(post,empId))
    empDB.commit()

def display(empId):
    query = "select * from emp where employeeId = %s"
    test_cursor.execute(query,(empId,))
    result = test_cursor.fetchone()  # Fetch the result
    return result


# add("id1","aman","9109413639","emmail", "student")
# promote("inter","id1")
# display("id1")