from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# In-memory storage for blog posts
blogs = []
next_id = 1

# Routes
@app.route('/')
def index():
    return render_template('index.html', blogs=blogs)

@app.route('/blogs/<int:blog_id>')
def blog_detail(blog_id):
    blog = next((blog for blog in blogs if blog['id'] == blog_id), None)
    if not blog:
        return "Blog not found", 404
    return render_template('blog_detail.html', blog=blog)

@app.route('/create-blog', methods=['GET', 'POST'])
def create_blog():
    global next_id
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        blog = {
            'id': next_id,
            'title': title,
            'content': content,
            'created_at': datetime.utcnow()
        }
        blogs.append(blog)
        next_id += 1
        return redirect(url_for('index'))
    return render_template('create_blog.html')

@app.route('/blogs/<int:blog_id>/edit', methods=['GET', 'POST'])
def edit_blog(blog_id):
    blog = next((blog for blog in blogs if blog['id'] == blog_id), None)
    if not blog:
        return "Blog not found", 404
    if request.method == 'POST':
        blog['title'] = request.form['title']
        blog['content'] = request.form['content']
        return redirect(url_for('blog_detail', blog_id=blog_id))
    return render_template('create_blog.html', blog=blog)

@app.route('/blogs/<int:blog_id>/delete', methods=['POST'])
def delete_blog(blog_id):
    global blogs
    blogs = [blog for blog in blogs if blog['id'] != blog_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
