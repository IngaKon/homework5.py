immutable_var= 1,2.5, 'солнце, земля'
print(immutable_var)
#immutable_var[1]=3
# В кортеже нельзя изменить элемент, так как кортеж не поддерживает обращение по элементам.
# Но если внутри кортежа есть список, тогда в этом списке можноменять элемент.
immutable_var= ([1,2.5], 'солнце, земля')
immutable_var[0][1]=2
print(immutable_var)
mutable_list=['огонь','вода','земля','облако',]
mutable_list[3]='воздух'
mutable_list.append('True')
print(mutable_list)