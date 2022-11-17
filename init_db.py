import sqlite3

conn = sqlite3.connect('we1.db')
engine = conn.cursor()

create_table_sql="""
CREATE TABLE shop (
	shirt_id int, 
	shirt_name char, 
	shirt_price int, 
	link char,
	item_count int,
	current_owner char
)
"""

engine.execute(create_table_sql)
conn.commit()

insert_records="""
INSERT INTO shop (shirt_id, shirt_name, shirt_price, link, item_count, current_owner) 
VALUES (0, "Fundamentals", .05, "https://images-na.ssl-images-amazon.com/images/I/71Zg2d9QG2S._AC_UX466_.jpg", 5, "0x6a7F0Cc12f30C905C3139395aC1Bbf7c294e9dcd"),
	   (1, "Rosie The Riviter", .06, "https://m.media-amazon.com/images/I/A13usaonutL._CLa%7C2140%2C2000%7C918Dsd9GtiL.png%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_AC_UX679_.png", 2, "0x6a7F0Cc12f30C905C3139395aC1Bbf7c294e9dcd"), 
	   (2, "RBG", .07, "https://i.etsystatic.com/36271525/r/il/d3b13d/4006850366/il_1588xN.4006850366_sys0.jpg", 4, "0x6a7F0Cc12f30C905C3139395aC1Bbf7c294e9dcd"),
	   (3, "Codess", .08, "https://res.cloudinary.com/teepublic/image/private/s--adJ33DFv--/t_Resized%20Artwork/c_crop,x_10,y_10/c_fit,h_576/c_crop,g_north_west,h_626,w_470,x_-39,y_-25/g_north_west,u_upload:v1462829024:production:blanks:a59x1cgomgu5lprfjlmi,x_-434,y_-350/b_rgb:eeeeee/c_limit,f_auto,h_630,q_90,w_630/v1589371695/production/designs/10105194_0.jpg", 20, "0x6a7F0Cc12f30C905C3139395aC1Bbf7c294e9dcd")
"""		

engine.execute(insert_records)
conn.commit()

select_data = """
SELECT * FROM shop
"""

engine.execute(select_data)
print(engine.fetchall())
conn.commit()
conn.close()