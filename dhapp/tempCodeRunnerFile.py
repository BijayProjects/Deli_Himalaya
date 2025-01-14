
        ddd = datetime.datetime.now()
        return render(request, 'main/home.html',{'ddd':ddd})
