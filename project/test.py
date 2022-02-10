import dbModule

db = dbModule.Database()

input_id = input()
input_h = input()
sql = "SELECT * FROM test"
sql1 = "INSERT INTO test(sample2, sample3) VALUES ('%s', '%s')" %(input_id, input_h)
db.execute(sql1)
db.commit()
result = db.executeAll(sql)
for rst in result:
    print(rst['sample1'])
    print(rst['sample2'])
    print(rst['sample3'])