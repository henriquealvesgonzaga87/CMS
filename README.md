# CMS (Content Management System)

This is a Content Management System (CMS) project built with Python and Django. The CMS provides a platform for managing and publishing content on websites. It offers a user-friendly interface for creating, editing, and organizing various types of content such as articles, blog posts, pages, and more.

## Features

- User authentication and role-based access control.
- Create, edit, and delete content items.
- Categorize and tag content items for easy organization and retrieval.
- WYSIWYG editor for rich text content creation.
- Media management for uploading and handling images, videos, and other files.
- SEO-friendly URLs and metadata customization for improved search engine visibility.
- Responsive design for optimal viewing experience across different devices.
- Customizable templates and themes for easy customization of the website's appearance.
- Plugin system for extending the functionality of the CMS.

## Technologies Used

- Backend: [Python](https://www.python.org/), [Django](https://www.djangoproject.com/), [SQLite](https://www.sqlite.org/)
- Frontend: [HTML](https://html.com/), [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS), [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript), [Bootstrap](https://getbootstrap.com/)
- Authentication: [Django Authentication](https://docs.djangoproject.com/en/3.2/topics/auth/)
- Rich Text Editor: [Django CKEditor](https://django-ckeditor.readthedocs.io/)
- File Uploads: [Django File Uploads](https://docs.djangoproject.com/en/3.2/topics/http/file-uploads/)
- SEO: [Django SEO](https://djangoseo.com/)
- Testing: [Django Testing](https://docs.djangoproject.com/en/3.2/topics/testing/)

## Getting Started

### Prerequisites

- Python (3.6 or higher)
- Django (3.2 or higher)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/henriquealvesgonzaga87/CMS.git
```

2. Install dependencies:

```bash
cd CMS
pip install -r requirements.txt
```

3. Configure the database:
   
   - Open the `settings.py` file located in the `config` directory.
   - Update the database settings according to your setup (e.g., change the database engine, name, username, and password).

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open your browser and visit `http://localhost:8000` to access the CMS.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request describing your changes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [OpenAI](https://openai.com/) for providing the GPT-3.5 model used to generate this README.
- [GitHub](https://github.com/) for hosting and version control.
- [Python](https://www.python.org/) and [Django](https://www.djangoproject.com/)
