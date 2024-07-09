from django.http import JsonResponse
import json

def job_detail_view(request):
    job_data = [
        {
            "jobtitle": {
                "h1": "Junior Software Developer"
            },
            "job_image": {
                "img": "https://media.istockphoto.com/id/477994952/sv/foto/dedicated-to-the-deadline.jpg?s=612x612&w=0&k=20&c=LAGa0h8tkH24igtwG9Gt8tG2SB89KQtYv5qU53spHGQ=",
                "width": "100%"
            },
            "logo": {
                "img": "https://coredination.zendesk.com/hc/theming_assets/01HZPBVPJQM6AARZ5SPR6QGEB0",
                "width": "30px"
            },
            "job_description": {
                "p": "Entry-level position focusing on coding, debugging, and collaboration within a development team. Requires basic knowledge of programming languages and problem-solving skills."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
            },
            "job_image": {
                "img": "https://media.istockphoto.com/id/1056253870/sv/foto/snygg-gammal-man-arbetar-p%C3%A5-b%C3%A4rbar-dator-surfa-p%C3%A5-internet-i-staden-utomhus-i-digital-nomad.jpg?s=612x612&w=0&k=20&c=zGm7f1HbdLA6YOsyKd0-G5E55D5UXrVAd_tquQT4lhA=",
                "width": "100%"
            },
            "logo": {
                "img": "https://coredination.zendesk.com/hc/theming_assets/01HZPBVPJQM6AARZ5SPR6QGEB0",
                "width": "30px"
            },
            "job_description": {
                "p": "Lead frontend development projects, ensuring responsive and user-friendly interfaces. Expertise in HTML, CSS, JavaScript, and modern frameworks required."
            }
        },
        {
            "jobtitle": {
                "h1": "Project Manager"
            },
            "job_image": {
                "img": "https://media.istockphoto.com/id/871133990/sv/foto/att-s%C3%A4tta-sina-huvuden-ihop.jpg?s=612x612&w=0&k=20&c=42S7g8GC8C9IgVwQtPkraib3eJoeADVECLO0ytbCK6Q=",
                "width": "100%"
            },
            "logo": {
                "img": "https://coredination.zendesk.com/hc/theming_assets/01HZPBVPJQM6AARZ5SPR6QGEB0",
                "width": "30px"
            },
            "job_description": {
                "p": "Oversee project lifecycle from planning to delivery. Coordinate teams, manage budgets, and ensure timely completion of projects."
            }
        },
        {
            "jobtitle": {
                "h1": "Data Analyst"
            },
            "job_image": {
                "img": "https://media.istockphoto.com/id/1383479265/sv/foto/doctors-work-at-the-office-at-night-on-a-pc.jpg?s=612x612&w=0&k=20&c=fYM3XaknMnikqjrXnBmdZa8P0u8LCbSuzuMOOmcoZ5c=",
                "width": "100%"
            },
            "logo": {
                "img": "https://coredination.zendesk.com/hc/theming_assets/01HZPBVPJQM6AARZ5SPR6QGEB0",
                "width": "30px"
            },
            "job_description": {
                "p": "Interpret complex data sets to provide actionable insights. Proficiency in statistical software and strong analytical skills are essential."
            }
        },
        {
            "jobtitle": {
                "h1": "Marketing Specialist"
            },
            "job_image": {
                "img": "https://media.istockphoto.com/id/181086342/sv/foto/why-not-use-this-copyspace-its-free.jpg?s=612x612&w=0&k=20&c=9BSiLIKYW-l51QoD4wMP1PNt9WFGn1rYF9xo7ohrr3U=",
                "width": "100%"
            },
            "logo": {
                "img": "https://coredination.zendesk.com/hc/theming_assets/01HZPBVPJQM6AARZ5SPR6QGEB0",
                "width": "30px"
            },
            "job_description": {
                "p": "Develop and execute marketing campaigns. Strong communication skills and understanding of market trends are necessary."
            }
        },
    ]
    return JsonResponse(job_data, safe=False)
