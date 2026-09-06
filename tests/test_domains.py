from fedtwin.domains.profiles import DOMAIN_PROFILES, domain_target

def test_all_domains_have_eight_dimensional_targets():
    assert len(DOMAIN_PROFILES)==7
    assert all(len(domain_target(d))==8 for d in DOMAIN_PROFILES)
