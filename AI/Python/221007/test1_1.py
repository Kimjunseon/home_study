# 22년 9월 30일 (금)

person = {"name" : "kim" , 'money' : 50000.0}
person2 = {"name" : "park" , 'money' : 30000.0}
list = [person, person2]
print("%s과 %s의 합의 평균은 %d원 입니다." %(person.get("name"), person2.get("name"), (person.get('money')+person2.get('money'))/len(list)))
print("%s과 %s의 합의 평균은 %d원 입니다." %(person2.get("name"), person.get("name"), (person.get('money')+person2.get('money'))/2))
print("%s과 %s의 합의 평균은 %d원 입니다." %(person.get("name"), person2.get("name"), (person.get('money')+person2.get('money'))/2))