{
    'name' : 'Hospital' ,
    'version' :'12.0.1.0.0',
    'category':'Extra Tools',
    'summary':'first module',
    'author':'Mohammed Hany',
    'depends':['base'],
    'data':[
        'views/base_menu.xml',
        'security/ir.model.access.csv',
        'views/doctors_view.xml',
        'views/patients_view.xml'

     ],
    'installable':True,
    'application':True,

}