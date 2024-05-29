from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_paragraphs = int(request.form['num_paragraphs'])
        return render_template('paragraphs.html', num_paragraphs=num_paragraphs)

    return render_template('index.html')

@app.route('/result', methods=['POST'], endpoint='result_endpoint')
def result():
    num_paragraphs = int(request.form['num_paragraphs'])
    title = request.form['title']
    category = request.form['category']
    tags = request.form['tags']
    slug = request.form['slug']
    author = request.form['author']
    paragraphs = [request.form[f'paragraph_{i}'] for i in range(num_paragraphs)]

    date = datetime.now().strftime('%Y-%m-%d %H:%M')

    markdown_content = f"---\nTitle: {title}\nDate: {date}\nCategory: {category}\nTags: {tags}\nSlug: {slug}\nAuthor: {author}\n---\n\n"
    
    for i, paragraph in enumerate(paragraphs):
        markdown_content += f"# Paragraph {i+1}\n\n{paragraph}\n\n"

    return render_template('result.html', markdown_content=markdown_content)

if __name__ == '__main__':
    app.run(debug=True)
