import arrow

from kardashev import factories



# Mind tests
def test_it_should_have_augmentations():
    mind = factories.MindFactory.build()
    assert 'SharedHost' in mind.augmentations
    from kardashev.resources import cloud
    assert isinstance(mind.augmentations['SharedHost'], cloud.SharedHost)

def test_it_should_increment_a_field():
    mind = factories.MindFactory.build()
    assert mind.power == 1
    mind2 = mind.increment(power=1)
    assert mind2 is not mind
    assert mind2.power == 2

    mind3 = mind2.increment(power=20)
    assert mind3 is not mind2
    assert mind3.power == 22


def test_it_should_decrement_a_field():
    mind = factories.MindFactory.build(power=22)
    assert mind.power == 22
    mind2 = mind.decrement(power=1)
    assert mind2 is not mind
    assert mind2.power == 21

    mind3 = mind2.decrement(power=20)
    assert mind3 is not mind2
    assert mind3.power == 1
    
    
def test_it_should_sleep():
    start = arrow.Arrow(2017, 1, 1)
    mind = factories.MindFactory.build(date=start)
    assert mind.date == start
    mind2 = mind.sleep()
    assert mind2 is not mind
    assert mind2.date == start.replace(seconds=1)
