# E-CAD: Electronic Cadastral Management System

[![Django](https://img.shields.io/badge/Django-2.2.3-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![GeoDjango](https://img.shields.io/badge/GeoDjango-GIS-orange.svg)](https://docs.djangoproject.com/en/stable/ref/contrib/gis/)

A comprehensive web-based Electronic Cadastral Management System built with Django and GeoDjango for managing and visualizing land parcel data, buildings, transportation networks, and hydrological features.

## 🌟 Features

- **Land Parcel Management**: Complete cadastral data management with parcel boundaries, ownership details, and registration information
- **Building Information**: Detailed building records with geometric data and parcel associations
- **Transportation Networks**: Road and transportation infrastructure mapping
- **Hydrological Features**: Water bodies and drainage system management
- **GIS Integration**: Full Geographic Information System capabilities with spatial data handling
- **Web Interface**: User-friendly web interface for data visualization and management
- **Admin Panel**: Django admin interface for data administration

## 🏗️ Project Structure

```
E-CAD/
├── src/                          # Main application source code
│   ├── ecad/                     # Django project configuration
│   │   ├── data/                 # Shapefile data storage
│   │   │   ├── Building/         # Building shapefiles
│   │   │   ├── Hydro/           # Hydrological shapefiles
│   │   │   ├── Parcel/          # Land parcel shapefiles
│   │   │   └── Transportation/   # Transportation shapefiles
│   │   ├── settings.py          # Django settings
│   │   ├── urls.py              # URL configurations
│   │   └── wsgi.py              # WSGI configuration
│   ├── pages/                   # Main pages app
│   ├── shapefiles/              # GIS data models and utilities
│   │   ├── models.py            # GIS data models
│   │   ├── load_shp.py          # Shapefile loading utilities
│   │   └── views.py             # Views for shapefile data
│   ├── static/                  # Static files (CSS, JS, images)
│   ├── templates/               # HTML templates
│   └── manage.py               # Django management script
├── Include/                     # Python header files
├── Lib/                        # Python libraries and dependencies
├── Scripts/                    # Executable scripts
└── LICENSE.txt                 # License information
```

## 🛠️ Technical Stack

- **Backend**: Django 2.2.3
- **GIS Framework**: GeoDjango with PostGIS support
- **Database**: SQLite (development) / PostgreSQL with PostGIS (production)
- **Frontend**: HTML5, CSS3, JavaScript
- **Spatial Data**: Shapefile support for GIS data import
- **Admin Interface**: Django Admin with GIS capabilities

## 📊 Data Models

### Parcel Model
- Object ID and unique parcel key
- Owner information and registration details
- Adjacent parcel references (North, South, East, West)
- Shape area calculations
- MultiPolygon geometry (SRID: 4326)

### Building Model
- House numbers and parcel associations
- Shape length and area measurements
- MultiPolygon geometry for building footprints

### Transportation Model
- Named transportation features
- Shape measurements and area calculations
- MultiPolygon geometry for transportation networks

### Hydro Model
- Named hydrological features
- Hydro type classification
- Shape measurements and geometry data

## 🚀 Installation

### Prerequisites
- Python 3.x
- GDAL/OGR libraries
- PostGIS (for production)
- Django 2.2.3
- GeoDjango dependencies

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/ro-hit81/E-CAD.git
   cd E-CAD
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django==2.2.3
   pip install psycopg2-binary  # For PostgreSQL
   # Install GDAL and other GIS dependencies based on your system
   ```

4. **Configure database**
   - Update `src/ecad/settings.py` with your database configuration
   - For development, SQLite is pre-configured

5. **Run migrations**
   ```bash
   cd src
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Load GIS data**
   ```bash
   python manage.py shell
   >>> from shapefiles.load_shp import *
   >>> parcel_run()
   >>> building_run()
   >>> transportation_run()
   >>> hydro_run()
   ```

7. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

## 🎯 Usage

### Web Interface
- Access the main application at `http://localhost:8000`
- View the cadastral homepage with project information
- Navigate through different sections of the application

### Admin Interface
- Access Django admin at `http://localhost:8000/admin`
- Manage parcel, building, transportation, and hydro data
- View and edit spatial data through the GIS-enabled admin interface

### Data Management
- Import new shapefile data using the loading utilities
- View spatial data with geometric properties
- Manage cadastral records with ownership and registration details

## 🔧 Development

### Adding New Features
1. Create new Django apps for additional functionality
2. Define GIS models in `models.py`
3. Create corresponding loading utilities for shapefile data
4. Update URL configurations and create views
5. Add templates for frontend display

### Customization
- Modify templates in `src/templates/` for UI changes
- Update static files in `src/static/` for styling
- Extend models in respective apps for additional data fields

## 📝 API Documentation

The application uses Django's built-in admin interface for data management. For custom API development:

- Use Django REST Framework for API endpoints
- Implement GeoJSON serialization for spatial data
- Add authentication and permissions as needed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project uses the Python Software Foundation License. See [LICENSE.txt](LICENSE.txt) for details.

## 👨‍💻 Author

**Rohit Khati** - [ro-hit81](https://github.com/ro-hit81)

## 🙏 Acknowledgments

- Django and GeoDjango communities
- Python Software Foundation
- Final Year Project supervision and guidance
- Open source GIS libraries and tools

## 📞 Support

For support and questions:
- Create an issue in the GitHub repository
- Contact the project maintainer

---

**Note**: This is a final year project demonstrating electronic cadastral management capabilities using modern web GIS technologies.
