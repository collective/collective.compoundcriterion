.. image:: https://travis-ci.org/IMIO/collective.compoundcriterion.svg?branch=master
   :target: https://travis-ci.org/IMIO/imio.compoundcriterion

.. image:: https://coveralls.io/repos/IMIO/collective.compoundcriterion/badge.png?branch=master
  :target: https://coveralls.io/r/IMIO/collective.compoundcriterion?branch=master



====================
collective.compoundcriterion
====================

This package add a new kind of criterion available for plone.app.collection.

Motivation
----------

Sometimes, some index are composed of different elements with a certain logic or you need to query particular elements of the site like groups of the current user or anything else.
This is not achievable using default indexes and Collection UI, you need to write python code.

How to use
----------

When adding/editing a Collection, a new criterion filed under the 'Other' category of available indexes called 'Filter' is available.

When selecting a 'Filter', a selection box will show you named adapter that provide the collective.compoundcriterion.interfaces.ICoumpondCriterionFilter interface.

You will be able to select among available ones.  This can still be used together with other criteria.

To register this complex query builder named adapter, you will have to add this kind of code :

.. code:: xml

   <adapter for="plone.app.collection.interfaces.ICollection"
            factory="collective.compoundcriterion.tests.adapter.CompoundCrietrionFilterAdapter"
            provides="collective.compoundcriterion.interfaces.ICoumpondCriterionFilter"
            name="testing-compound-adapter" />
 
Such an adapter is available in the testing part, so, adding the code above to your configure.zcml will make it possible to test the functionnality.
