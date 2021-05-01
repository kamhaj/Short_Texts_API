## Application using API calls to display/create/edit/delete short texts (Posts). </br></br>

## Django + DRF utilized.
## Tests run using PyTest.
</br></br>
## Deployed on Heroku
base page: 	**https://kamhaj-short-texts.herokuapp.com/api/short_texts/**

</br>

## API usage:
1.  GET - to get details on specified (by id) Post </br></br>
 authentication required: No </br>
 response code on success: 200 </br>
 URL scheme: /api/short_texts/post/post_details/<int:pk> </br>
 example URL: https://kamhaj-short-texts.herokuapp.com/api/short_texts/post/post_details/1 </br>
 request fields: - </br>
	
  ```bash
	response_body_example = {
								"title": "Dummy title",
								"content":"Dummy content.",
								"views_counter": 7
							}
   ```
  
additional info: </br>
                  1. no body required </br>
                  2. views_counter is updated by +1 every time resource is requested. </br>
					        3. pk - primary key (id) </br>
           
2. POST - to create a new Post </br></br>
	authentication required: Yes (Token) </br>
	response code on success: 201 </br>
	URL scheme: /api/short_texts/post </br>
	example URL: https://kamhaj-short-texts.herokuapp.com/api/short_texts/post </br>
	request fields: title, content </br>
	
  ```bash
	request_body_example = 	{
								"title": "New title",
								"content":"New content."
							}
  ```
  ```bash            
  response_body_example = 	{
								"title": "New title",
								"content":"New content.",
                "views_counter": 0
							}
  ```
   
3. PUT - to update existing Post </br></br>
	authentication required: Yes (Token) </br>
	response code on success: 200 </br>
	URL scheme: /api/short_texts/post/<int:pk> </br>
	example URL: https://kamhaj-short-texts.herokuapp.com/api/short_texts/post/1 </br>
	request fields: title, content </br>
	
  ```bash
	request_body_example = 	{
								"title": "Updated title",
								"content":"Updated content."
							}
  ````
  
additional info: </br>
                1. pk - primary key (id) </br>
	
4. DELETE - to delete existing Post </br></br>
	authentication required: Yes (Token) </br>
	response code on success: 204 </br>
	URL scheme: /api/short_texts/post/<int:pk> </br>
	example URL: https://kamhaj-short-texts.herokuapp.com/api/short_texts/post/1 </br>
	request fields: - </br>
	
	additional info: </br>
                  1. no body required </br>
					        2. pk - primary key (id) </br>

</br></br>
## Deployed using Heroku CLI: (steps): </br>

1. Heroku login in CLI. <br/>
2. heroku git:remote -a kamhaj-short-texts (set git remote to https://git.heroku.com/kamhaj-short-texts.git). <br/>
	Use 'git remote -v' to check that we are in the right project (urls for fetch and push are displayed). <br/>
3. In Django project folder: <br/>
```bash
pip install gunicorn 
pip install whitenoise
```
  <br/>
4. Set up files that Heroku needs: 
		requirements.txt (automatically installed before app startup)
		runtime.txt (python version specified)
		Procfile (specify commands that are executed by the app on startup) 
    <br/>
5. In Django settings.py - add heroku to ALLOWED_HOSTS and change DEBUG to False (as well as for SECRET_KEY, use Heroku env. variables). <br/>
6. Add buildpack on Heroku (so it know which language we are using). <br/>
7. Update Git repository. Change repo to private. <br/>
8. On Heroku website, connect app to GitHub repository (Deploy Tab -> Connect to GitHub).  <br/>
9. In settings.py add STATIC_ROOT to let Heroku deal with static files (create folder for static files). <br/>
10. Create a staticfiles folder (add dummy file for it to work). It is gonna be a place for future static files needed.
11. Add django_heroku in settings.py (update requirements.txt).  <br/>
12. On Heroku website, hit 'Deploy Branch' button (main branch by default). <br/> 
    You can check logs for error using 'heroku logs --tail' in CLI.  <br/> 

<br/>

## DB - superuser creation:
1. In Heroku CLI: heroku git:remote -a kamhaj-short-texts
2. heroku run bash
3. heroku run python manage.py createsuperuser
4. If ISP is blocking port 5000, use CLI on Heroku website.
