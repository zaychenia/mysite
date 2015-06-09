__author__ = 'Olenka'

from myapp.models import Subject
from cStringIO import StringIO



subjects = []

def create_plan(spec, dep, chosen_list):
    log_out = StringIO()
    def log(obj):
        print >> log_out, obj
    to_remove = set([s.id for s in get_subjects_for_choice(spec, dep)]) - set(chosen_list)
    print len(Subject.objects.all()), len(to_remove)
    subjects = [s for s in Subject.objects.all() if s.id not in to_remove]
    print  len(subjects)
#  graph creation
    graph = []
    for i in xrange(0, len(subjects)):
        graph.append([0] * len(subjects))

    for i in xrange(0, len(subjects)):
        if subjects[i].depends_on:
            for j in map(int, subjects[i].depends_on.split(',')):
                graph[i][j - 1] = 1

    # print graph on the screen
    # for row in graph:
    #    log (' '.join(map(str, row)))


    #  fill Plan with subjects linked to semester
    s=[0,0,0,0,0,0,0,0]

    plan = []
    for d in xrange(0, len(subjects)):
        for y in xrange(1,9):
            if subjects[d].semestr == str(y):
                if subjects[d].department.name == dep:
                    if (subjects[d].specialization is None) or (subjects[d].specialization is int(spec)):
                        if (subjects[d].kredits + s[y-1]) <= (31):
                            s[y-1] = subjects[d].kredits + s[y-1]
                            plan.append(subjects[d])
                        else: log('Invalid data. Subjects linked to ' + str(y) + ' semester have exceeded maximum sum of credits')
    # add  opportunity to divide credits on both semesters if there are two of them


    ex = set()
    def fun(node):
        ex.add(node)
        for i in range(len(graph)):
            if graph[node][i] == 1 and i not in ex:
                fun(i)

        if subjects[node] not in plan and str(subjects[node].depends_on) == '':
            if subjects[node].department.name == dep:
                if (subjects[node].specialization is None) or (subjects[node].specialization is int(spec)):
                    y = 1
                    while (subjects[node].kredits + s[y-1]) > (30):
                        y = y+1
                    else:
                        s[y-1] = subjects[node].kredits + s[y-1]
                        plan.append(subjects[node])
                        plan[-1].semestr = y

        if (subjects[node] not in plan) and str(subjects[node].depends_on) != '':
            if subjects[node].department.name == dep:
                if (subjects[node].specialization is None) or (subjects[node].specialization is int(spec)):
                    d=(subjects[node].depends_on.split(','))
                    max=0
                    for a in range(0,len(d)):
                        v = subjects[int(d[a])-1].semestr
                        if v>max:
                            max=v
                    y = int(max)
                    while (subjects[node].kredits + s[y-1]) > (30):
                        y = y + 1
                    else:
                        s[y-1] = subjects[node].kredits + s[y-1]
                        plan.append(subjects[node])
                        plan[-1].semestr = y

    #choose nodes on which run fun(node) function
    for m in range(0,len(graph)):
        p = 0
        for n in range(0,len(graph)):
            if graph[m][n] == 1:
                p = p+1
        if p > 0:
            ex = set()
            fun(m)
        elif p == 0:
            q = 0
            for k in range(0,len(graph)):
                if graph[k][m] == 1:
                    q = q+1
            if q > 0:
                ex = set()
                fun(m)

    # fill Plan with independent subjects
    for i in xrange(0, len(subjects)):
        if subjects[i] not in plan:
            if subjects[i].department.name == dep:
                if (subjects[i].specialization is None) or (subjects[i].specialization is int(spec)):
                    for b in range(0,8):
                        if (subjects[i].kredits + s[b]) <= (30):
                            s[b] = subjects[i].kredits + s[b]
                            plan.append(subjects[i])
                            plan[-1].semestr = b+1
                            break

    norm = []
    za_spec = []
    obr = []

    for i in xrange(0, len(plan)):
        if plan[i].group == 1:
            norm.append(plan[i])
        if plan[i].group == 2:
            za_spec.append(plan[i])
        if plan[i].group == 3:
            obr.append(plan[i])

    log('wwwwwwwwwwwww')
    log(s[3])

    s1=s[0]
    s2=s[1]
    s3=s[2]
    s4=s[3]
    s5=s[4]
    s6=s[5]
    s7=s[6]
    s8=s[7]


    log (spec)

    log('Kilkist disciplin y plani - ')
    log(len(plan))
    log('Kilkist kreditiv y semestrah - ')
    log(s)
    for w in plan: log(w)

     #show subjects for choice to user


    #correct the plan


    return log_out.getvalue(),plan, norm, za_spec, obr, s1,s2,s3,s4,s5,s6,s7,s8



def get_subjects_for_choice(spec,dep):
    subjects = Subject.objects.all()

    choice_list = []
    for i in xrange(0, len(subjects)):
        if subjects[i].department.name == dep:
            if (subjects[i].specialization is None) or (subjects[i].specialization is int(spec)):
                if subjects[i].name.startswith('*'):
                    choice_list.append(subjects[i-1])
                    choice_list.append(subjects[i])

    return choice_list




