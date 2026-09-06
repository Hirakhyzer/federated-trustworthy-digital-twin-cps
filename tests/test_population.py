from fedtwin.domains.population import make_population

def test_population_cycles_domains():
    c=make_population(14,0,1)
    assert len({x.domain for x in c})==7
