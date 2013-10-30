=======================
 Framework Frustration
=======================

At work we use two frameworks, Django_ and CherryPy_. The decision to
use one or the other typically comes down to who is starting the
project and, to a lesser extent, whether the app is primarily a user
facing app or an API. For example, if we need to put together an app
to show off some data publically, Django is our go to framework. If we
are creating an internal REST API for other services, CherryPy is
typically the way to go.

Developers typically feel more comfortable with one framework. I'm
definitely a CherryPy guy, while the rest of the folks on my team fall
on the Django side of the fence. The result is that I'm often working
on Django code, which ends up being pretty frustrating.

First off, the nice thing about Django is that if you commit to the
ecosystem and learn it, there is a wealth of 80% tools you can use to
create a functional web app. This is true of any opinionated full
stack framework and I'd consider Django a prime example. When you
understand Django, you can get a lot of stuff done.

The problem is that when you *don't* know Django, getting things done
is challenge. The reason being is that the framework hides general
python techniques in order to hide complexity. As I said, when you
understand what happens under the hood, hiding the complexity is
fine. The problem is that many full stack frameworks, such as Django,
don't make it easy to look under the hood and follow the stack to the
necessary code.

CherryPy, on the other hand, makes uncovering the layers of complexity
much easier. You can typically isolate bits of the framework
relatively easily and test them in a prompt or simple script to
discover issues. The source code is also small enough that diving into
its algorithms is not unreasonable. Sure, the documentation is
lacking, there are fewer high quality plugins and you will probably
have to make more decisions as to how to implement common idioms, but
the result is that uncovering the logic is rarely a problem.

Personally, I like CherryPy because you can take the codebase and
figure what is going on. When you do hit frameworks such as
sqlalchemy_ or templates such as mako_ or jinja2_, the documentation
is typically of a high quality because of the smaller set of topics
that need covering. Also, while it is possible to create CherryPy
specific integration points, it is just as easy to write your own
classes and functions to hide complexity as the need arises.

It can be frustrating working on Django because it is difficult to
peel back the layers. For example, we use Tastypie_ for some API
endpoints. It is exceptionally nice for exposing models. You get
pagination, multiple authentication schemes, and a whole host of other
bits that are nice. That said, when you need to adjust the API, it is
cumbersome and produces somewhat ugly code. Here is an example, from
the docs. ::

  class ParentResource(ModelResource):
      children = fields.ToManyField(ChildResource, 'children')

      def prepend_urls(self):
          return [
              url(r"^(?P<resource_name>%s)/(?P<pk>\w[\w/-]*)/children%s$" % (self._meta.resource_name, trailing_slash()), self.wrap_view('get_children'), name="api_get_children"),
          ]

      def get_children(self, request, **kwargs):
          try:
              obj = self.cached_obj_get(request=request, **self.remove_api_resource_names(kwargs))
          except ObjectDoesNotExist:
              return HttpGone()
          except MultipleObjectsReturned:
              return HttpMultipleChoices("More than one resource is found at this URI.")

          child_resource = ChildResource()
          return child_resource.get_detail(request, parent_id=obj.pk)

First off, you have to understand a suite of concepts. Tastypie
generates URL regexes for you. You can override these via the
`prepend_urls` method. Second, the `get_children` method contains some
custom exceptions that come from Django core that are caught in order
to return tastypie specific error return values. Finally, the
`get_detail` method is a helper that automatically will render the
object found in `get_children` method and return a proper tastypie
response.

As you begin to understand the code it is not a huge mystery what is
happening. With that said, there is a lot of reading that has to
happen before you can begin to understand what is really going on. You
also have to understand the implicit barriers between tastypie and
django. Finally, these are all on a semi-magic set of `Resource`
objects that inject into the list of URL patterns, removing the
benefit of having all your URLs in one place.

Hopefully it is clear how trying to understand and debug this type of
code is challenging and can be frustrating. While it hides a great
deal of complexity for you and adds many feature that you may or may
not need, it presents a chasm between the code and the actual impact
that must be crossed by reading documentation.

At this point I should mention that this kind of code is a pet peeve
of mine because it is difficult to maintain. Someone approaching this
code without a strong background in Django and Tastypie would have to
spend a good amount of time gettig up to speed before being able to
try and fix a bug. What's more, that person would not be able to
simply open up Python prompt or write a test without further reading
about what specialized tools are available and how to use
them. Obviously, it is not a waste of time to make the investment, but
for me personally, I'd rather learn by writing code, isolating
functionality and writing tests than reading docs, hoping they are up
to date.


.. _Django: http://djangoproject.com
.. _CherryPy: http://cherrypy.org
.. _sqlalchemy: http://www.sqlalchemy.org
.. _mako: http://www.makotemplates.org
.. _jinja2: http://jinja.pocoo.org/docs/
.. _Tastypie: http://tastypieapi.org/



.. author:: default
.. categories:: code
.. tags:: python, django, programming
.. comments::
