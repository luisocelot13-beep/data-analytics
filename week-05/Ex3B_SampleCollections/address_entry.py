Contact_info = {'address': '1306 kelston pl','city': 'Charlotte','state': 'NC','zipcode': '27107'}

full_name = {'First_name': 'Luis','Last_name': 'Ocelotl'}

full_name.update({'honorific':'MR.'})

Contact_info.update(full_name)

print(f'{Contact_info['honorific']} {Contact_info['First_name']} {Contact_info['Last_name']}')


# print(Contact_info['address'],'\n' , Contact_info['city'],Contact_info['state'],',','\n', Contact_info['zipcode']) 
# either way i prefer f string

print(f'{Contact_info['address']}\n'
      f'{Contact_info['city']}\n'
      f'{Contact_info['state']}\n'
      f'{Contact_info['zipcode']}')

