<h2 align="center">URL Shorting API</h3>
<hr>

<h3>Repo goal</h4>
<p>Develop a URL shortening API that will take a long URL and return a short URL. The short URL should redirect to the long URL.</p>

<br>

<h3>API Endpoints</h3>
<ul>
  <li>POST / -d {"initial_url": some_url}</li>
  <li>GET /:shortUrl</li>
</ul>

<br>

<h3>How to run</h3>
<p>1. Clone the repository</p>
<p>2. Run <code>pip install -r requirements.txt</code> to install the dependencies</p>
<p>3. Run <code>python manage.py migrate</code> to migrate database</p>
<p>4. Run <code>python manage.py runserver</code> to start the server</p>

TEST