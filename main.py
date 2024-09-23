from flet import 
import sqlite3

coon = sqlite3.connect("DaTa.db",check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""" CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    stdname Text,
    stdphone Text,
    stdphone Text,
    stdaddress Text,
    stmathmatic INTEGER,
    starabic INTEGER,
    stenglish INTEGER,
    stchemistry INTEGER,
    stgeography INTEGER,
    stalive INTEGER,
    stphysics INTEGER,
    stHoly Quran INTEGER,
    stislamic INTEGER,
    stdate INTEGER,
    stcommunity INTEGER
) """)
conn.commit()

 


def main (page:Page):
    page.title = 'Gwad'
    page.scroll = 'auto'
    page.wnindow.top =1
    page.wnindow.left =960
    page.wnindow.width = 390
    page.wnindow.height = 740
    page.bgcoolor = 'white'
    page.theme_mode = Theme_Mode.LIGHT

    ###################################

    tabe_name = 'student'
    query = f'SELECT COUNT(*) FROM {tabe_name}'
    cursor.execute(query)
    result = cursor.fetchone()
    row_count = result[0]

    def add(e):
        cursor.execute("INSERT INTO student (stdname,stdname,stdphone,stdaddress,stmathmatic,starabic,stenglish,stchemistry,stchemistry,stgeography,stalive,stphysics,stHoly Quran,stislamic,stdate,stcommunity) VALUES(?.?.?.?.?.?.?.?.?.?.?.?.?.?.?)",(tname.value,tphone.value,tphone.value,taddress.value,mathmatic.value,arabic.value,english.value,chemistry.value,geography.value,alive.value,physics.value,Holy Quran.value,VALUESislamic.value,date.value,community.value))
        conn.commit()
    def show(e):
        page.clean()
        c = conn.cursor()
        c.execute("SELECT * FROM student")
        users = c.fetchall()
        print(users)

        if not users =="":
            keys = ['id','stdname','stdphone','stdphone','stdaddress','stmathmatic','starabic','stenglish','stchemistry','stgeography','stalive','stphysics','stHoly Quran','stislamic','stdate','stcommunity']
            resyut = [dict(zip(keys,values)) for values in users ]
            for x in result:

                ############ marks #########
                m =x['stmathematics']
                a =x['starabic']
                e =x['stenglish']
                b =x['stchemistry']
                g =x['stgeography']
                l =x['stalive']
                p =x['stphysics']
                h =x['stHoly Quran']
                i =x['stislamic']
                d =x['stdate']
                c =x['stcommunity']
                res = m + a + E + b + g + l + p + h + i + d + c 
                if res < 50 :
                    a = Text('راسب',size=19,color='red')
                if res > 50 :
                    a = Text('ناجح',size=19,color='green')



            page.add(
                card(
                    color='black',
                    content=container(
                        content=column([
                           ListTile(
                               leadiing = Icon (icons.PERSON),
                               title=Text('Name : '+x['stdname'],color='white'),
                               subtitle = Text('رقم هاتف الطالب : '+x['stdphone'],color='amber')
                           ),
                            Row([
                                Text('رقم هاتف اخر للطالب : '+x['stdphone'],color='green'),
                                Text('عنوان سكن الطالب : '+x['stdaddress'],color='green'),
                            ],alignment=MainAxisAlignment.CENTER),
                            Row([
                                Text('رياضيات : '+ str(x['stmathematics']),color='blue'),
                                Text(' عربي : '+ str(x['starabic']),color='blue'),
                                Text('انجليزي : '+ str(x['stenglish']),color='blue'),
                            ],alignment=MainAxisAlignment.END),
                            Row([
                                Text('كيمياء : '+ str(x['stchemistry']),color='blue'),
                                Text('جغرافياء : '+ str(x['stgeography']),color='blue'),
                                Text('احياء : '+ str(x['stalive']),color='blue'),
                            ],alignment=MainAxisAlignment.END),
                            Row([
                                Text('فيزياء : '+ str(x['stphysics']),color='blue'),
                                Text('قران كريم : '+ str(x['stHoly Quran']),color='blue'),
                                Text('اسلامية : '+str(x['stislamic']),color='blue'),
                            ],alignment=MainAxisAlignment.END),
                            Row([
                                Text('تاريخ: '+ str(x['stdate']),color='blue'),
                                Text('مجتمع: '+ str(x['stcommunity']),color='blue'),
                            ],alignment=MainAxisAlignment.END),

                            Row([
                                a 
                            ],alignment=MainAxisAlignment.CENTER),
                        ])
                    )
                )
            )
            page.update()

   ############# Feils ################
   tname = TextField(label='اسم الطالب',icon=icons.PERSON,rtl=True,height=38)
   tphone =TextField(label='رقم هاتف ولي امر الطالب',icon=icons.PHONE,rtl=True,height=38)
   tphone =TextField(label='رقم هاتف الطالب',icon=icons.PHONE,rtl=True,height=38)
   taddress =TextField(label='عنوان سكن الطالب',icon=icons.LOCATION_CITY,rtl=True,height=38)
########################################

################## marks ###############
marktext = Text("Marks student - علامات الطالب",text_align='center',weight='bold')
mathmatic = TextField(label='رياضيات',width=110,rtl,height=38)
arabic = TextField(label='عربي',width=110,rtl,height=38)
english = TextField(label='انجليزي',width=110,rtl,height=38)
chemistry = TextField(label='كيمياء',width=110,rtl,height=38)
geography = TextField(label='جغرافيا',width=110,rtl,height=38)
alive = TextField(label='احياء',width=110,rtl,height=38)
physics = TextField(label='فيزياء',width=110,rtl,height=38)
Holy Quran = TextField(label='قران كريم',width=110,rtl,height=38)
islamic = TextField(label='اسلامية',width=110,rtl,height=38)
date = TextField(label='تاريخ',width=110,rtl,height=38)
community = TextField(label='مجتمع',width=110,rtl,height=38)
#########################################

addbuttn = ElevatedButton(
    "عرض كل الطلاب",
    width=170,
    style=ButtonStyle(bgcolor='blue',color='white',padding=15),
    on_click=show
)

showbuttn = ElevatedButton(
    "اضافة طالب جديد",
    width=170,
    style=ButtonStyle(bgcolor='blue',color='white',padding=15),
    on_click=add
)


page.add(
    Row([
        Image(src="VID_20240823_091018_943.mp4",width=280)
        ],alignment=MainAxisAlignment.CENTER),

    Row([
        Text("تطبيق الطالب والمعلم في جيبك",size=20,font_family="Simple Jut Out",color='black')
        ],alignment=MainAxisAlignment.CENTER),

        Row([
        Text(" عدد الطلاب المسجلين : ",size=20,font_family="Simple Jut Out",color='blue'),
        Text(row_count,size=20,font_family="Simple Jut Out",color='black'),
        ],alignment=MainAxisAlignment.CENTER,rtl=True),
        tname,
        tphone,
        tphone,
        taddress,


    Row([
        marktext
        ],alignment=MainAxisAlignment.CENTER,rtl=True),

    Row([
        mathmatic,arabic,english
    ],alignment=MainAxisAlignment.CENTER,rtl=True),

    Row([
        chemistry,geography,alive
        ],alignment=MainAxisAlignment.CENTER,rtl=True),

    Row([
        physics,Holy Quran,islamic
        ],alignment=MainAxisAlignment.CENTER,rtl=True),

    Row([
        date,community
        ],alignment=MainAxisAlignment.CENTER,rtl=True),

    Row([
        addbuttn,showbuttn
        ],alignment=MainAxisAlignment.CENTER,rtl=True),

)


    app(main)