# @app.get("/sqlalchemy")
# def get_posts(db: Session = Depends(get_db)):
#     sqlquery=db.query(models.Post)
#     print(sqlquery)
#     posts = sqlquery.all()
#     if not posts:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"posts does not exist")

#     return posts

# @app.get("/sqlalchemy/{id}",response_model=schemas.Post)
# def get_post(id: int, db: Session = Depends(get_db)):
#     sqlquery=db.query(models.Post).filter(models.Post.id==id)
#     print(sqlquery)
#     post = sqlquery.first()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id {id} does not exist")

#     return post

# @app.post("/createpost", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
# def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), ):
#     # cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
#     #                (post.title, post.content, post.published))
#     # new_post = cursor.fetchone()

#     # conn.commit()
  
#     print(post.dict())
#     new_post = models.Post(**post.dict())
#     print(new_post)
#     sqladd=db.add(new_post)
#     print(sqladd)
#     db.commit()
#     db.refresh(new_post)

#     return new_post


# @app.put("/PostUpdate/{id}", response_model=schemas.Post)
# # @app.put("/PostUpdate/{id}")
# def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db), ):

#     # cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",
#     #                (post.title, post.content, post.published, str(id)))

#     # updated_post = cursor.fetchone()
#     # conn.commit()

#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     print(post_query)  

#     post = post_query.first()

#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")

#     # if post.owner_id != current_user.id:
#     #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#     #                         detail="Not authorized to perform requested action")

#     sqlupdate=post_query.update(updated_post.dict(), synchronize_session=False)
#     print(sqlupdate)
#     db.commit()

#     return post_query.first()

# @app.delete("/sqlalchemy/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int, db: Session = Depends(get_db), ):

#     # cursor.execute(
#     #     """DELETE FROM posts WHERE id = %s returning *""", (str(id),))
#     # deleted_post = cursor.fetchone()
#     # conn.commit()
#     post_query = db.query(models.Post).filter(models.Post.id == id)
#     print(post_query)
#     post = post_query.first()
#     print(post)
#     if post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} does not exist")

#     # if post.owner_id != current_user.id:
#     #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
#     #                         detail="Not authorized to perform requested action")

#     post_query.delete(synchronize_session=False)
#     db.commit()

#     return Response(status_code=status.HTTP_204_NO_CONTENT)

# @app.post("/user", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

#     # hash the password - user.password
#     hashed_password = utils.hash(user.password)
#     user.password = hashed_password

#     new_user = models.User(**user.dict())
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user

# @app.get("/user/{id}",response_model=schemas.UserOut)
# def get_post(id: int, db: Session = Depends(get_db)):
#     sqlquery=db.query(models.User).filter(models.User.id==id)
#     print(sqlquery)
#     user = sqlquery.first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"user with id {id} does not exist")

#     return user

# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_db_posts(post: PostBase):
#     cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """,
#                    (post.title, post.content, post.published))
#     new_post = cursor.fetchone()

#     conn.commit()
#     return {"data":post}

# @app.post("/createposts")
# def create_posts(payload: PostBase):
#     print(payload)
#     # return {"new_post": f"title: {payload['title']} content: {payload['content']}"}
#     return {"data":payload}

# @app.get("/posts/{id}")
# def get_post(id: int):
#     cursor.execute("""SELECT * from posts WHERE id = %s """, (str(id)))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"post with id: {id} was not found")

#     return post

# @app.get("/allposts")
# def get_posts():
#     cursor.execute("""SELECT * FROM products """)
#     posts = cursor.fetchall()
#     return{"data": posts}