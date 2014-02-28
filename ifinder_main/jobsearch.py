from ifinder_main.models import Job

def get_job_list(max_results=0, contains=''):
    job_list = []

    if contains:
        job_list = Job.objects.filter(job_name__contains=contains)
    else:
        job_list = Job.objects.all()


    if max_results > 0:
        if len(job_list) > max_results:
            job_list = job_list[:max_results]

    return job_list