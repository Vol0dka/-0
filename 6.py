#Ввод суммы
sum = float(input('Сумма заказа в ресторане '))
#Рассчет чаевых
chai = 0.18*sum
#Рассчет налога
nalog = 0.2*sum
#Вывод итога
print('Налог: ',format(nalog, '.2f')+'₽\n' 'Чаевые: ',format(chai, '.2f')+'₽\n' 'Итог: ', format((sum-chai-nalog), '.2f')+"₽\n")