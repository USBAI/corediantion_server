from django.http import JsonResponse

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
                "p": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Molestias quo eum magni optio corporis in accusamus. Vitae possimus, animi adipisci nesciunt quos expedita magnam reiciendis voluptas amet, molestias odio velit?"
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Senior Frontend Developer"
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
                "p": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae ultricies justo, in vehicula velit. Nulla facilisi. Nullam id convallis est."
            }
        },
        {
            "jobtitle": {
                "h1": "Product Manager"
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
                "p": "Sed tempor eu lorem sed ultricies. Nam vitae magna et mauris eleifend tempor. Duis vel libero urna."
            }
        }
    ]
    return JsonResponse(job_data, safe=False)
