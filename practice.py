from flask import Flask, render_template_string

app = Flask(__name__)

home_page = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Learn Python</title>
    <style>
      body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f4f7fb; }
      header { background: #306998; color: white; padding: 20px; text-align: center; }
      main { padding: 20px; max-width: 800px; margin: auto; }
      section { background: white; padding: 20px; margin-bottom: 20px; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
      h2 { color: #333; }
      ul { line-height: 1.6; }
      a { color: #306998; text-decoration: none; }
      a:hover { text-decoration: underline; }
    </style>
  </head>
  <body>
    <header>
      <h1>Learn Python</h1>
      <p>A simple website for beginners who want to learn Python.</p>
    </header>
    <main>
      <section>
        <h2>Start Here</h2>
        <p>Welcome! This site gives you a quick introduction to Python basics with examples and resources.</p>
      </section>
      <section>
        <h2>Topics</h2>
        <ul>
          <li><strong>Variables</strong> - store values</li>
          <li><strong>Data types</strong> - strings, numbers, lists, dictionaries</li>
          <li><strong>Control flow</strong> - if, for, while</li>
          <li><strong>Functions</strong> - reusable code blocks</li>
          <li><strong>Modules</strong> - extend Python with libraries</li>
        </ul>
      </section>
      <section>
        <h2>Example</h2>
        <pre><code>name = input('What is your name? ')
print(f'Hello, {name}! Welcome to Python learning.')
</code></pre>
      </section>
      <section>
        <h2>Resources</h2>
        <ul>
          <li><a href="https://www.python.org/" target="_blank">Official Python website</a></li>
          <li><a href="https://docs.python.org/3/tutorial/" target="_blank">Python Tutorial</a></li>
          <li><a href="https://www.w3schools.com/python/" target="_blank">W3Schools Python</a></li>
        </ul>
      </section>
    </main>
  </body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_page)

if __name__ == '__main__':
    app.run(debug=True)
