# #1st project start
#
# import pandas as pd
#
# Employee= {'Number' :[1,2,3,4,5],'Name':["Nafisa","Nahid","Tabassum", "Jeba", "Hasan"],'Hourly selary':[15,25,35,45,50]}
#
# table1 = pd.DataFrame(Employee)
# print(table1.head(3))
# print(table1.tail(3))
#
# #end


# # 2nd project start


# import pandas as pd
#
# food1 = {'Numbers':[1,2,3,4,5],'Name' :["apple","banana","jackfood","Mango","Milk"],'Peice':[2,4,6,8,10]}
# food2 = {'Numbers':[1,2,3,4,5],'Name' :["kathal","banana","jackfood","Mango","Milk"],'Peice':[2,6,6,8,120]}
# table1 = pd.DataFrame(food1)
# table2 = pd.DataFrame(food2)
#
# fusion = pd.merge(table1,table2,on ="Numbers")
# print(fusion)

# #end


# # 3rd project start
#
# import pandas as pd
#
# food1 = {'Numbers':[1,2,3,4,5],'Name':["apple","Banana","Mango","Orange","Jack-food"],'Price':[100,200,300,400,500]}
# food2 = {'Color':["Red","yellow","Light-Red","Orange","Light-Yellow"],'Weight':[120,220,320,430,234],'Qt':[1,2,3,4,5]}
# table1 = pd.DataFrame(food1)
# table2 = pd.DataFrame(food2)
#
# fusion2= table1.join(table2)
# print(fusion2)
# # end


# # 4th project start
#
#
#
# import pandas as pd
#
# color =pd.read_csv('C:\\Users\\User\\OneDrive\\Desktop\\python\\python project.csv')
# color.to_html("Nicecolor")
#
#
# # end