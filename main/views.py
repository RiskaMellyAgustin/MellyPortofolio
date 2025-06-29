from django.shortcuts import render
from django.urls import reverse


def home(request):
    projects = [
        {
            "title": "Smart Dropout & Anomalies Detection",
            "description": "Prediksi dropout & deteksi anomali berdasarkan log aktivitas LMS mahasiswa.",
            "image": "img/pict_avg.jpg",
            "icon": "🤖",
            "detail_url": reverse('project_dropout'),
            "github": "https://github.com/RiskaMellyAgustin/DATA-SCIENCE-PROJECT-EXAM",
            "stack": ["Python", "Django", "XGBoost", "PostgreSQL", "Chart.js"],
        },
        {
            "title": "Orders Dashboard (Looker Studio)",
            "description": "Visualisasi interaktif pemesanan berdasarkan segmentasi & tren menggunakan Looker Studio.",
            "image": "img/looker_dashboard.jpg",
            "icon": "📊",
            "detail_url": reverse('project_looker'),
            "github": "https://lookerstudio.google.com/reporting/c49e7945-23bf-48a1-ac28-050e97b39b66",
            "github_icon": "🌐 View",
            "stack": ["Looker Studio", "Google Sheets"],
        },
        {
            "title": "Revenue Cycle System",
            "description": "Sistem manajemen langganan dan invoice berbasis Django + Chart.js.",
            "image": "img/pict_acc.jpg",
            "icon": "💰",
            "detail_url": reverse('project_revenue'),
            "github": "https://github.com/RiskaMellyAgustin/NETFLIX-PROJECT-REVENUE",
            "stack": ["Django", "Chart.js", "PostgreSQL", "TailwindCSS"],
        },
        {
            "title": "Dormitory Report Website",
            "description": "Aplikasi pencatatan laporan asrama mahasiswa secara online & mobile-friendly.",
            "image": "img/pict_dorm.jpg",
            "icon": "🏠",
            "detail_url": reverse('project_dormitory'),
            "github": "https://github.com/RiskaMellyAgustin/DormitoryReport_Website",
            "stack": ["Laravel","PHP","Bootstrap", "mySQL"],
        },
        {
            "title": "PUMA App (Flutter)",
            "description": "Aplikasi manajemen kegiatan organisasi mahasiswa berbasis Flutter & Firebase.",
            "image": "img/pict_puma.jpg",
            "icon": "📱",
            "detail_url": reverse('project_puma'),
            "github": "https://github.com/RiskaMellyAgustin/puma_flutter_app",
            "stack": ["Flutter", "Firebase", "Dart"],
        }
    ]
    return render(request, 'main/home.html', {"projects": projects})


# def home(request):
#     return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def project_revenue(request):
    return render(request, 'main/project_revenue.html')

def project_dropout(request):
    return render(request, 'main/project_dropout.html')

def project_dormitory(request):
    return render(request, 'main/project_dormitory.html')

def project_puma(request):
    return render(request, 'main/project_puma.html')

def project_looker(request):
    return render(request, 'main/project_looker.html')


# def projects(request):
#     return render(request, "main/projects.html")

def contact(request):
    return render(request, "main/contact.html")
