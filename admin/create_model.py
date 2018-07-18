from admin.db_manager import db, cursor

cursor.execute("""create table question(
	q_id integer primary key autoincrement,
    q_text text not null,
    q_rank smallint not null,
    q_type smallint not null default 1
)""")

cursor.execute("""create table answer(
	a_id integer primary key autoincrement,
    a_text varchar(200) not null,
    a_is_correct boolean
)""")

cursor.execute("""create table answer_to_question(
	a_id integer references answer(a_id),
    q_id integer references question(q_id)
)""")

cursor.execute("""create table answers_rank(
    a_id integer references answer(a_id),
    a_rank smallint not null
)""")

db.commit()
