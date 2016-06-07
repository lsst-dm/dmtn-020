.. vim: ts=3:sts=3

:tocdepth: 1

This document provides an informal guide to the everyday mechanisms
underpinning LSST Data Management's approach to project management. It is
intended to be read in conjunction with :ldm:`472`, which provides a formal
description of the project management process and requirements.

Important Documents
===================

Wherever a conflict arises, baselined project documentation takes precedence
over this note. You are encouraged to submit bug reports so that this document
can be made compliant.

Be aware of prefixes: “LDM-” documents refer specifically to the Data
Management subsystem, “LSE-” to Systems Engineering, “LPM-” to Project
Management.

:lpm:`43`, :lpm:`44`
   *WBS Structure* and *WBS Dictionary*, respectively. The former shows the
   overall work breakdown structure for the whole project.

:lpm:`98`
   *LSST Project Controls System Description*. Describes and defines the
   components of the :term:`PMCS` used to manage and report on the overall
   LSST Project.

:ldm:`472`
   *LSST DM Project Management and Tools*. The formal, high-level document
   which defines the project management process used by LSST DM. The present
   document may be thought of as a guide to applying the principles defined
   in :ldm:`472` in practice.

In addition, you should be familiar with the `EVMS Training – CAM 101`_
presented by the :ref:`Project Controls Specialist <sec-contacts>` at the
`LSST 2014 Meeting`_. `Slides are available as a PDF`_ for easy reference.

.. _EVMS Training – CAM 101: https://project.lsst.org/meetings/lsst2014/node/100
.. _LSST 2014 Meeting: https://project.lsst.org/meetings/lsst2014/
.. _Slides are available as a PDF: _static/EVMS_Training.pdf

.. _sec-contacts:

Useful Contacts
===============

The LSST DM Project Manager is Jacek Becla. He is the first point of contact
for all issues regarding project management within DM.

The LSST Project Controls Specialist is Kevin Long. He is responsible for the
:term:`PMCS` and, in particular, for ensuring that DM properly complies with
our earned value management requirements. He is the first point of contact for
all questions about the PMCS system.

Technical Managers
==================

This guide is primarily aimed at the LSST DM technical managers. Technical
managers report directly to the DM Project Manager. Per :ldm:`472`, they are
expected to:

- Assemble the team capable of delivering work scoped through the :term:`WBS`
  on-time and within budget. Provide daily technical management and leadership
  for the team, monitor and optimize team performance.

- Work closely with the DM Project Manager on defining short and long-term
  plan and schedule for their teams. Direct the execution of their team's
  plan, ensuring the team delivers on-time and within budget.

- Report group's activities as required, including reporting to the
  :term:`EVMS` used by LSST, and providing input for monthly status reports.

In short, technical managers are, in general, expected to act as :term:`CAM`
and technical lead for their groups; as such, they are sometimes referred to
as “T/CAMs”. The role of CAM is defined in detail :ref:`below
<sec-structure>`.

.. _sec-structure:

Formal Organizational Structure
===============================

.. _sec-wbs:

Work Breakdown Structure
------------------------

The LSST :term:`WBS` is defined in :lpm:`43` (see also :lpm:`44` for an
extended—but not universally illuminating—definition of what each level of the
breakdown consists of).

The WBS provides a hierarchical index of all hardware, software, services, and
other deliverables which are required to complete the LSST Project. It
consists of alphanumeric strings separated by periods. The first component is
always “1”, referring the LSST Construction Project. “02C” in the second
component corresponds to Data Management Construction. Subdivisions thereof
are indicated by further digits. Subdivisions at this level correspond to
teams within the DM project. Thus:

======== ========================================= =======================
WBS      Description                               Lead Institution
======== ========================================= =======================
1.02C.01 System Management                         LSST
1.02C.02 Systems Engineering                       LSST
1.02C.03 Alert Production                          University of Washington
1.02C.04 Data Release Production                   Princeton University
1.02C.05 Science User Interface                    Caltech IPAC
1.02C.06 Science Data Archive                      SLAC
1.02C.07 Processing Control & Site Infrastructure  NCSA
1.02C.08 International Communications. & Base Site NCSA & LSST
1.02C.09 Systems Integration & Test                LSST
1.02C.10 Science Quality & Reliability Engineering LSST
======== ========================================= =======================

These subdivisions are referred to as the *third level WBS*. Often, they are
quoted without the leading “1” (e.g. “02C.01”), but, even in this form, they
are referred to as “third level”.

All of these third level WBS elements are subdivided, forming a fourth level.
The fourth level always contains a “00” element, which is used to capture
management and :ref:`sec-loe`, and may contain other fourth level, or even
deeper, structure. Nodes in the WBS tree are referred to as :term:`element`\s.

.. _sec-obs:

Organization Breakdown Structure
--------------------------------

In parallel with the WBS, we have an :term:`OBS`, which assigns each
institution involved in the project a unique numeric identifier. The OBS is
defined in :lpm:`98`. Those institutions directly relevant to DM include:

==== ========================
OBS  Institution
==== ========================
1.01 LSST
1.02 SLAC
1.03 Caltech IPAC
1.04 NCSA
1.05 University of Washington
1.06 Princeton University
==== ========================

The Control Account Manager
---------------------------

A :term:`control account` is the intersection between the WBS and the OBS.
Each control account falls under the purview of a :term:`CAM`. Typically
within DM, a single CAM is responsible for the whole of a third level WBS. That
is, the manager at the lead institution for a particular component is
responsible for all work performed on that WBS element, even if that work is
performed at another institution.

.. _sec-evms:

Earned Value Principles
=======================

LSST DM is funded by as an :term:`NSF` :term:`MREFC` project. Under the terms
of the MREFC award, we are required to follow an *earned value* approach to
project management. A full description of the earned value approach is outside
the scope of this document (the project will provide formal training). We
provide a brief aide-mémoire for convenience only.

The earned value technique assigns each component of the system with a dollar
value corresponding to its expected cost of production. In a (largely)
software based project like LSST DM, it is often convenient to equate the cost
of production with the cost of the labor required to write the code: in the
more general case, however, it also includes cost of hardware procurements,
etc. This provides a convenient heuristic for estimating cost: given some
nominal labor costs, the cost of a component is a proxy for the amount of
labor required to produce it.

As well as a cost, the plan includes a start date and a completion date
for each component.

The total value of work which *should* have been completed by a particular
date is the :term:`BCWS`. The total value of work which has *actually* been
completed by the date is the :term:`BCWP`. The total sum expended on the work
is the :term:`ACWP`. If estimates of both cost and time for every component
of the system are accurate, at the end of construction, all of these three
quantities will be equal.

In practice, estimation is rarely perfect. Imperfect estimates are exposed as
variances. Specifically, we can show either :term:`SV` (defined as BCWP-BCWS;
a negative value means that less of the system has been delivered to date than
planned) or :term:`CV` (defined as BCWP-ACWP; a negative value means that the
work delivered to date has been more expensive than predicted). Related
quantities, :term:`SPI` and :term:`CPI`, express the same information as
ratios rather than sums. In general, we strive to achieve variances of near
zero: even a positive variance (corresponding being ahead of schedule or being
cheaper than expected) is indicative of an inaccurate plan.

All of these indices can be applied to any WBS element within the project.
Thus, we can talk about value earned across the whole of DM (1.02C) or on a
specific component (say, the User Workspace Toolkit, 1.02C.05.05).

.. _sec-labor-costs:

Labor Costs
-----------

Our methodology is designed to avoid exposing individual salaries to the wider
project. Therefore, when calculating labor costs for earned value purposes, we
do not rely on a known cost per individual. Instead, all staff are assigned to
one of a small number of types (scientist, senior scientist, developer, senior
developer), each of which is assigned a nominal cost level according to
institution: it does not vary between individuals of the same type within the
same institution. This nominal cost does not, therefore, correspond to a
particular individual, but is a broadly defined expectation. See :lpm:`81` for
details.

.. _sec-variance-narrative:

Variance Narratives
-------------------

Every month, the :term:`eCAM` tool is updated from PMCS to reflect the latest
earned value status. If either cost or schedule is behind schedule by more
than either $100,000 or 10% you are required to provide a “narrative”. This is
divided into two parts: you must explain why the variance arose, and what
action will be taken to correct it (e.g. slipping work into the future, or
diverting resources from elsewhere to make up the shortfall). The narrative is
entered directly into eCAM.

.. note::

   In future, narratives may also be required for positive variances (i.e.
   running ahead of schedule).

Variance is calculated on a monthly basis; variance narratives are due in the
second week of the calendar month following that to which they apply (refer to
the :ref:`sec-monthly-cycle` for details).

.. _sec-loe:

Level of Effort Work
--------------------

The implicit assumption in the earned value technique outlined above is that
all work corresponds to a specific deliverable. However, parts of our work do
not: every member of the team will find it necessary to attend meetings or
take part in other activities which do not directly map to deployed code. This
may be particularly the case for technical managers or others in leadership
roles within the project. This work is referred to as :term:`LOE`: it is
assumed to earn value simply through the passage of time.

:ldm:`472` provides a detailed definition of the types of work it is
permissible to regard as LOE. In general, we strive to minimize the fraction
of our effort which is devoted to LOE activities and favour those which are
more directly accountable.

The assumption encoded in :ldm:`472` is that developers will spent 30% of
their time on LOE type activities, and the remaining 70% of their effort is
tracked against concrete deliverables.

All LOE work should be invoiced to the “00” fourth-level WBS element
(1.02C.03.00, 1.02C.04.00, etc), which is reserved for “management engineering
and integration”. Per the :ref:`effort estimation procedure <sec-effort>`,
this means that *at least* 30% of every individual's time will be invoiced to
the 00 element.

.. _sec-effort:

Estimating Effort
=================

The Project assumes that a full-time individual works for a total of 1,800
hours per year: this figure is *after* all vacations, sick leave, etc are
taken into account. Staff appointed to “developer” positions are expected to
devote this effort directly to LSST.

Appointment as a “scientist” includes a 20% personal research time allowance.
That is, scientists are expected to devote 1,440 hours per year to LSST, and
the remainder of their time to personal research.

.. note::

   Personal research time is *not* chargeable to LSST under any WBS or
   account. In particular, it is not counted as level of effort. The Project
   expects to pay the full rate for an individual with research time who
   contributes 1,440 hours to the project, and does not require any accounting
   of the remaining 360 hours. See also the discussion in :lpm:`81` section 7.

.. note::

   Some individuals serve roles within DM which are referred to as
   “scientist”, such as the Project Scientist and Pipelines Scientist. These
   roles are not equivalent to being granted personal research time, but
   reflect a level of scientific oversight within the project. Time spent
   performing this role must be accounted for in the usual way (either as LOE
   or as providing deliverables), and charged to an account agreed with the
   :ref:`DM Project Manager <sec-contacts>`.

Our base assumption is that 30% of an individual's LSST time (i.e. 540
hours/year for a developer, 432 hours/year for a scientist) are devoted to
overhead for meetings, ad-hoc discussions and other interruptions. This work
is counted as :term:`LOE` (and, as such, is charged to the relevant “00”
fourth level WBS element, as described :ref:`here <sec-loe>`).

Some individuals—notably technical managers themselves, as well as others in
leadership roles—are expected to have a larger fraction of their time devoted
to :term:`LOE` work.

Assuming no variation throughout the year, we therefore expect 105 hours of
productive work from a developer, or 84 hours from a scientist, per month.
Note that this is averaged across the year: some months, such as those
containing major holidays, will naturally involve less working time than
others: the remainder will necessarily include more working time to
compensate.

Rather than working in hours, our :term:`JIRA` based system uses “story
points” (:term:`SP`\s), with one SP being defined as equivalent to four hours
of effort by a competent developer. Thus, we expect developers and scientists
to produce 26.25 and 21 SPs per *average* month respectively. This is
summarized in :numref:`tab-working-rate`.

.. _tab-working-rate:

.. table:: Expected working rates for developers and scientists.

   +-----------+----------------------+---------------+
   |           | Hours                | SPs Per Month |
   +           +----------+-----------+               |
   |           | Per Year | Per Month |               |
   +===========+==========+===========+===============+
   | Developer | 1800     | 105       | 26.25         |
   +-----------+----------+-----------+---------------+
   | Scientist | 1440     | 84        | 21            |
   +-----------+----------+-----------+---------------+

On occasion, it may be appropriate to tailor the number of SPs expected per
unit time from a particular individual. For example:

- Individuals in leadership roles may assign a larger fraction of their time
  to LOE type work, and therefore spend fewer hours generating SPs. The ratio
  of hours to story points remains constant, but the number of hours
  decreases.
- New or inexperienced developers, even when devoting their full attention to
  story-pointed work, will likely be less productive than their more
  experienced peers. In this case, the ratio of hours to SPs increases, but
  the number of hours remains constant.

In either case, the total number of SPs which will will be generated by the
team in a given time interval is reduced. This should be taken into account
when :term:`resource loading`.

.. _sec-long-term-plan:

Long Term Planning
==================

Refer to :ldm:`472` for a description of the long-term planning system. In
brief, the plan for the duration of construction is embodied in:

#. A series of *planning packages*, which describe major pieces of technical
   work. Planning packages are associated with concrete, albeit high-level,
   deliverables (in the shape of milestones, below), and have specific
   resource loads (staff assignments), start dates, and durations. The entire
   DM system is covered by around 100 of these planning packages.
#. *Milestones* represent the delivery or availability of specific
   functionality. Each planning package culminates in a milestone, and may
   contain other milestones describing intermediate results.

Planning packages are defined at the fourth level of the WBS breakdown (e.g.
at 1.02C.04.02, see the material on the :ref:`sec-wbs`). They may not cut
across the WBS structure, but rather must refer to that particular
fourth-level element and its children.

Milestones are defined at a number of levels: see :ldm:`472` for details. To
summarize:

Level 1
   These are chosen by the :term:`NSF`.

Level 2
   These reflect cross-subsystem commitments. As such, they must be defined in
   consultation with the DM Project Manager.

Level 3
   These reflect cross-third-level WBS commitments. As such, they must be
   defined in discussion between two or more technical managers.

Level 4
   These are internal to a particular third-level WBS, and can therefore be
   specified by a single technical manager.

Some of these are exposed to external reviewers: it is vital that these be
delivered on time and to specification. Low-level milestones are defined for
use within DM, but even here properly adhering to the plan is vital: your
colleagues in other teams will use these milestones to align their schedules
with yours, so they rely on you to be accurate.

.. _sec-long-term-research:

Planning Research Work
----------------------

In order for the DM system to reach its science goals, new algorithmic or
engineering approaches must sometimes be researched. It is appropriate to
budget time for this research work in planning packages. However, areas where
successful delivery of the DM system is dependent on speculative research are
a source of :term:`risk`: wherever possible, the plan should also provide for
a fallback option to be taken when research objectives are not achieved. When
fallback options are not available, discuss how to account for this risk with
the :ref:`DM Project Manager <sec-contacts>`.

.. _sec-long-term-value:

Earned Value and Planning Packages
----------------------------------

A planning package has a duration and a staff assignment (it is “resource
loaded”). Given a (nominal) cost per unit time of the staff involved (see
:ref:`sec-labor-costs`), this translates directly to a :term:`BCWS`.

During :ref:`sec-cycle-plan`, effort is drawn from the budget embodied in the
planning packages to generate the :term:`cycle` plan, described in terms of
epics: see :ref:`sec-planning-epics` for details. Each epic itself has a
particular budget. This budget is subtracted from that available in the
planning package at the point when the epic is defined.

At any given time, the :term:`BCWP` of a planning package consists of the
sum of the BCWP of all epics derived from that package which have been marked
complete, together with the fractions of value earned from all epics currently
in progress.

An example may serve to illustrate.

Planning package ``P`` is baselined to start at the beginning of F17 and run
through to the end of F18, i.e. a total of three cycles, or 18 months. It has
two members of staff\—``A`` and ``A``\— assigned to it full time. Both share the same
nominal cost of ``$X`` per cycle.

The BCWS for the total planning package is the cost per cycle multiplied by
the number of cycles: ``3 * $2X = $6X``.

In F17, both members of staff are assigned to six-month epic derived from
``P``. The BCWS of the epic is ``$2X``. The remaining value in the planning
package is ``$4X``.

At the end of F17, the epic is completed. The BCWP and ACWP are both ``$2X``.
The work is on cost and on schedule: there is no variance.

In S18, ``A`` is reassigned and is unable to work on a new epic derived from
``P``. ``B`` continues the work alone, completing an epic worth ``$X`` by the
end of the cycle. The BCWP and ACWP are now both ``$3X``; there is no cost
variance.  However, the BCWS is ``$4X``: compared to the original schedule for
the planning package, there is a schedule variance of ``-$X``. There is a
total of ``$3K`` left in the planning package.

In F18, ``C`` joins the project. ``C`` only costs ``$0.5X`` per cycle, but is
a fast worker: she can complete in one cycle work that would take ``A`` or
``B`` two cycles.

``B`` and ``C`` work together through F18. The ACWP for the cycle is
``$1.5X``; the BCWP is ``$3X``. The ACWP to date ``$4.5X``. The BCWP and BCWS
are both ``$6X``. At this point, the project is complete: there is no schedule
variance, and a cost variance of ``+$1.5X``.

.. _sec-cycle-plan:

Short Term Planning
===================

Per :ldm:`472`, short term planning is carried out in blocks referred to as
:term:`cycle`\s, which (usually) last for six months. Before the start of a
cycle, technical managers work with the DM Project Manager and the Project
Controls Specialist to ensure their plan for the cycle is well defined in both
:term:`JIRA` and :term:`PMCS`.

Defining The Plan
-----------------

Scoping Work
^^^^^^^^^^^^

The first essential step of developing the short term plan is to produce an
outline of the programme of work to be executed. In general, this should flow
directly from the :ref:`long term plan <sec-long-term-plan>`, ensuring that
the expected planning packages are being worked on and milestones being hit.

While developing the cycle, please:

- Do not add *artificial* padding or buffers to make the schedule look good;
- Do budget appropriate time for handling bugs and emergent issues;
- Reserve time for planning the following cycle: it will have to be defined
  before this cycle is complete;
- Leave time for other necessary activities, such as cross-team collaboration
  meetings and writing documentation.

Obviously, ensure that the programme of work being developed is achievable by
your team in the time available: ultimately, you will want to compare the
:ref:`number of SPs your team is able to deliver <sec-effort>` with the sum of
the SPs in the :ref:`epics <sec-planning-epics>` you have scheduled, while
also considering the skills and availability of your team. It is better to
under-commit and over-deliver than vice-versa, but, ideally, aim to estimate
accurately.

.. _sec-planning-epics:

Defining Epics
^^^^^^^^^^^^^^

As described in :ldm:`472`, the plan for a six month cycle fundamentally consists
of a set of resource loaded :term:`epic`\s defined in JIRA. Each epic loaded
into the plan must have:

- A concrete, well defined deliverable *or* be clearly described as a “bucket”;
- The ``cycle`` field set to the appropriate cycle;
- The ``WBS`` field set to the appropriate WBS *leaf* element.
- The ``Story Points`` field set to a (non-zero!) estimate of the effort
  required to complete the epic in terms of :term:`SP`\s (see :ref:`above
  <sec-effort>`).

Be aware that:

- An epic may only be assigned to a single cycle. It is not possible to define
  an epic that crosses the cycle boundary (see :ref:`sec-cycle-close` for the
  procedure when an epic is not complete by the end of the cycle).
- An epic may only be assigned to a single WBS leaf element. It is not
  possible to define epics that cover multiple WBS elements. See
  :ref:`sec-cross-team` for information on scheduling work which requires
  resources from multiple elements.
- An epic must descend from a single planning package (see
  :ref:`sec-long-term-plan`).
- Although :ref:`LOE work should be charged to the 00 fourth-level element
  <sec-loe>`, this does not imply that other work cannot be charged here.
  Indeed, where possible management activities *should* be scheduled as epics
  with concrete deliverables in this element rather than being handled as LOE.
- The epic should be at an appropriate level of granularity. While short epics
  (a few SPs) may be suitable for some activities, in general epics will
  describe a few months of developer-time. Epics allocated multiple hundreds
  of story points are likely too broad to be accurately estimated.

The :ref:`Project Controls Specialist <sec-contacts>` will :ref:`periodically
<sec-monthly-cycle>` pull information from JIRA to populate :term:`PMCS` with
the plan.

.. note::

   All epics which have WBS and cycle defined will be loaded into PMCS (and
   must, therefore, have concrete deliverables and plausible SP estimates).
   Epics which do not satisfy these criteria may be defined in JIRA. These
   will not be pulled into PMCS, will not form part of the scheduled plan, and
   will not earn value. However, they may still be useful for organizing other
   work, sketching plans for future cycles, etc: please define them as
   necessary.

In order to fully describe the plan to PMCS, epics require information that is
not captured in JIRA. Specifically, it is necessary to define:

- Start and end dates for the epic;
- Staff assignments.

.. note::

   Although it is possible—indeed, encouraged—to set the ``assignee`` field in
   JIRA to the individual who is expected to carry out the bulk of the work in
   an epic, this does not provide sufficient granularity for those cases when
   more than one person will be contributing.

.. note::

   In fact, it is only required to provide a staff assigment in terms of
   “resource types” (i.e. scientists, senior scientists, developers, senior
   developers, etc). In practice, to ensure your team is evenly loaded, it is
   usually necessary to break it down to named individuals.

This information is most conveniently captured in per-team spreadsheets which
are supplied to the Project Controls Specialist before the start of the
cycle. Spreadsheets describing previous cycles are stored in `Google Drive`_:
a convenient way to get started would be to use one of those as a template.

The spreadsheets used capture epic start and end dates at monthly granularity.
This can lead to a :ref:`variance <sec-evms>` when monthly results are
tabulated (it assumes that work for an epic is evenly distributed across all
the months in which it is scheduled). In practice, this variance is likely to
be small, and should average out by the end of the cycle, when all epics
should be closed on schedule. However, if this becomes a problem, it is
possible to fine-tune dates by directly consulting with the Project Controls
Specialist.

.. note::

   When loading epics at the start of a cycle, it is not necessary that they
   be fully :ref:`loaded with stories <sec-defining-stories>`: these can be
   defined during the cycle. You do, of course, need to have thought through
   the contents of the epic in enough detail to provide an overall SP
   estimate and deliverables, though.

.. _Google Drive: https://drive.google.com/drive/u/0/folders/0BxgFbTQURmr6TmxXSm5Dc1JJWk0

.. _sec-research-epics:

Scheduling Research Work
^^^^^^^^^^^^^^^^^^^^^^^^

As discussed in :ref:`sec-long-term-research`, research is sometimes required
to meet our objectives. However, it is not a natural fit to our usual planning
process, as it is speculative in its nature: it is often impossible to produce
a series of logical steps that will lead to the required result. We
acknowledge, therefore, that scheduling an epic to deliver some particular new
algorithm based on the results of research is impossible: we cannot preduct
with any confidence when the breakthrough will occur.

We therefore schedule research in :term:`timebox`\ed epics: we allocate a
certain amount of time based on the resources available, rather than on an
estimate of time to completion. However, note that these timeboxed epics
should still provide concrete deliverables: they are not open-ended “buckets”
as discussed elsewhere. Since we cannot rely on the successful completion of
the research project as a deliverable, we instead require that a summary of
the research completed to date be delivered at the completion of the time
allocated. The presentation and format of this report will vary depending on
the nature of the research (a `technical note`_ is a likely option), and,
:ref:`as usual <sec-planning-epics>`, should be defined before the epic is
ingested to :term:`PMCS`.

.. _technical note: https://sqr-000.lsst.io/

.. _sec-bucket:

Bucket Epics
^^^^^^^^^^^^

Some work is “emergent”: we can predict in advance that it will be necessary,
but we cannot predict exactly what form it will take. The typical example of
this is fixing bugs: we can reasonably assume that bugs will be discovered in
the codebase and will need to be addressed, but we cannot predict in advance
what those bugs will be.

This can be included in the schedule by defining a “bucket” epic in which
stories can be created when necessary during the course of a cycle. Make clear
in the description of the epic that this is its intended purpose: every epic
should either have a concrete deliverable or be a bucket.

Bucket epics have some similarities with :term:`LOE` work. As such, we
acknowledge that they are necessary, but seek to minimize the fraction of our
resources assigned to them. If more than a relatively small fraction of the
work for a cycle is assigned to bucket epics, please consider whether this is
really necessary and appropriate.

.. _sec-sps-to-bcws:

Mapping SPs to BCWS
^^^^^^^^^^^^^^^^^^^

As discussed above, the amount of work to be performed is :ref:`estimated in
terms of SPs <sec-effort>`, while the :ref:`earned value <sec-evms>` system
accounts for work in terms of budgeted cost (:term:`BCWS`). In order to
estimate the value earned by completing an epic, it is necessary to map from
one to the other.

The outline of the calculation here is straightforward: SPs map to developer
hours. Given the :ref:`staff assignment <sec-planning-epics>` for the epic,
the number of hours scheduled per developer can be calculated. Given the
:ref:`nominal costs <sec-labor-costs>` associated with each developer, the
total labor cost can be estimated.

Therefore, we calculate the number of hours of each staffing grade being
assigned to the epic, multiply that by the cost per hour of that grade, and
that provides the cost of the work scheduled.

.. _sec-cross-team:

Cross Team Work
^^^^^^^^^^^^^^^

Planning epics are always assigned to a particular WBS leaf element: they do
not span elements or teams. It is therefore impossible to schedule a single
epic which covers cross-team work. There are two ways to approach this
problem:

- The technical managers for both teams to be involved in the work schedule
  epics separately, within their own WBS structure. They are responsible for
  agreeing start and end dates, deliverables and resourcing between
  themselves. From the point of view of the :term:`PMCS`, these epics are
  independent pieces of work which happen to be coincident.
- With agreement between technical managers, an individual may be detached
  from one team and explicitly work for another team for some defined period.
  One technical manager is therefore responsible for defining and scheduling
  their work. Their “home” manager will charge :ref:`actuals <sec-actuals>`
  against the WBS supplied by the manager manager of the receiving team.

Regardless of the approach taken, technical managers should be especially
careful to ensure that cross-team work is well defined. Usually, it is
convenient for a single manager to take ultimate responsibility for ensuring
that it is successfully delivered.

.. _sec-cycle-change:

Revising the Plan
-----------------

During the cycle, it is possible that changing circumstances will cause
reality not to exactly match with the plan. This will ultimately cause a
:ref:`variance <sec-evms>`, which should be avoided and which—if it becomes
significant enough—will require a narrative.

After the plan for the cycle has been entered into JIRA, it is under change
control: it can only be altered through a :term:`LCR` approved by the
:term:`CCB`. In order to reschedule (or remove entirely from the cycle) an
epic which has not yet started, the technical manager should work with the
:ref:`Project Controls Specialist <sec-contacts>` to prepare and submit an
appropriate LCR to the CCB. The CCB meets on the third Wednesday of the
calendar month; change requests must be submitted well in advance of this.
Therefore, it is advisable to take time early in the calendar month to review
epics due to start in the *following* month and to issue an LCR on them if
necessary.

Note that it is *not possible* to alter history by means of an LCR. That is,
if the scheduled start date of an epic is already in the past, it is not
possible to move it into the future using a change request. In this case,
there is no option but to carry the variance related to the late start of the
epic into the future, to describe that with :ref:`narratives
<sec-variance-narrative>` where necessary, and to attempt to address the
variance as soon as is possible.

Based on the above, it is clear that technical managers should closely track
performance relative to the plan throughout the cycle, and proactively file
change requests to avoid running variances wherever possible.

.. _sec-cycle-close:

Closing the Cycle
-----------------

Assuming everything has gone to plan, by the end of a cycle all deliverables
should be verified and the corresponding epics should be marked as “done”.
When an epic is marked as done, it is equivalent to having delivered the
required functionality. The total cost of that functionality—the :term:`BCWS`,
calculated as per :ref:`sec-sps-to-bcws`\—is now claimed as value earned.

Epics which are in progress at the end of the cycle cannot be closed until
they have been completed. These epics will spill over into the subsequent
cycle. It is *not* appropriate to close an in-progress epic with a concrete
deliverable until that deliverable has been achieved: instead, a variance will
be shown until the epic can be closed. Obviously, this will impact the labor
available for other activities in the next cycle. (This does not apply to
:ref:`bucket epics <sec-bucket>`, which are, by their nature,
:term:`timebox`\ed within the cycle).

Similar logic applies to epics which *have not been started*: if the planned
start date is in the past, they :ref:`can no longer be rescheduled
<sec-cycle-change>` by means of an :term:`LCR`. They must be completed at the
earliest possible opportunity; you will show a variance until this has been
done.

Execution
=========

Having :ref:`thus <sec-cycle-plan>` defined the plan for a cycle, we execute
it by means of a series of month-long sprints. In this section, we detail the
procedures teams are expected to follow during the cycle.

.. _sec-defining-stories:

Defining Stories
----------------

:ref:`Epics have already been defined <sec-planning-epics>` as part of the
cycle plan. However, the epic is not at an appropriate level for scheduling
day-to-day work. Rather, each epic is broken down into a series of
self-contained “stories”. A :term:`story` describes a planned activity worth
between a small fraction of a :term:`SP` and several SPs (more than about 10 is
likely an indication that the story has not been sufficiently refined). It
must be possible to schedule a story within a single sprint, so no story
should ever be allocated more than 26 SPs.

The process for breaking epics down into stories is not mandated. In some
circumstances, it may be appropriate for the technical manager to provide a
breakdown; in others, they may request input from the developer who is
actually going to be doing the work, or even hold a brainstorming session
involving the wider team. This is a management decision.

It is not required to break all epics down into stories before the cycle
begins: it may be more appropriate to first schedule a few exploratory stories
and use them to inform the development of the rest of the epic. However, it is
required that all stories which will be :ref:`worked in an upcoming sprint
<sec-sprinting>` are defined before the sprint starts.

Note that there is no relationship enforced between the SP total estimated for
the epic and the sum of the SPs of its constituent stories. It is therefore
possible to over- or under-load an epic. This will have obvious ramifications
for the schedule. See :ref:`sec-cycle-value` for its impact on earned value.

.. _sec-sprinting:

Sprinting
---------

Each team organizes its work around periods of work called :term:`sprint`\s. A
sprint comprises a defined collection of stories which will be addressed over
the course of the month. These stories are not necessarily (indeed, not
generally) all drawn from the same epic: rather, while epics divide the cycle
along logical grounds, sprints divide it along the time axes.

Broadly, executing a sprint falls into three stages:

#. Preparation.

   The team assigns the work that will be addressed during the sprint by
   choosing from the :ref:`pre-defined stories <sec-defining-stories>`. Each
   team member should be assigned a plausible amount of work, based on the
   per-story SP estimates and the likely working rate of the developer (see
   :ref:`sec-effort`).

   The process by which work is assigned to team members is a local management
   decision: the orthodox approach is to call a team-wide meeting and discuss
   it, but other approaches are possible (one-to-one interactions between
   developers and technical manager, managerial fiat, etc).

   Do not overload developers. Take vacations and holidays into account. The
   sprint should describe a plausible amount of work for the time available.

#. Execution.

   Daily management during the sprint is a local decision. Suggested best
   practice includes holding regular “standup” meetings, at which developers
   discuss their current activities and try to resolve “blockers” which are
   preventing them from making progress.

   Stories should be executed following the instructions in the `Developer
   Guide`_ as regards workflow, coding standards, review requirements, and so
   on. It is important to ensure that completed stories are marked as “done”:
   experience suggests that this can easily be forgotten as developers rush on
   to the next challenge, but it is required to enable us to properly
   :ref:`track earned value <sec-cycle-value>`.

   .. note::

      When completing a story we do not change the number of SPs assigned to
      it: the SP total reflects our initial estimate of the work involved, not
      the total time invested. This makes it possible to review the quality of
      our estimates at the end of the sprint.


   Avoid adding more stories to a sprint in progress unless it is unavoidable
   (for example, the story describes a critical bug that must be addressed
   before proceeding). A sprint should always stay current and should be
   up-to-date with reality; if necessary, already scheduled stories may be
   pushed out of a sprint as soon as it is obvious it is unrealistic to expect
   them to be completed.

#. Review.

   At the end of the sprint, step back and consider what has been achieved.
   What worked well? What did not? How can these problems be avoided for next
   time? Was your estimate of the amount of work that could be finished in the
   sprint accurate? If not, how can it be improved in future? Refer to the
   `burn-down chart`_ for the sprint, and, if it diverged from the ideal,
   understand why.

   Again, the form the review takes is a local management decision: it may
   involve all team members, or just a few.

We use :term:`JIRA`\'s `Agile`_ capabilities to manage our sprints. Each
technical manager is responsible for defining and maintaining their own agile
board. The board may be configured for either `Scrum`_ or `Kanban`_ style work
as appropriate: the former is suitable for planned development activities
(e.g. Science Pipelines development); the latter for servicing user requests
(e.g. providing developer support).

.. _Developer Guide: http://developer.lsst.io/
.. _burn-down chart: https://en.wikipedia.org/wiki/Burn_down_chart
.. _Agile: https://www.atlassian.com/software/jira/agile
.. _Scrum: https://en.wikipedia.org/wiki/Scrum_(software_development)
.. _Kanban: https://en.wikipedia.org/wiki/Kanban_(development)

.. _sec-epic-done:

Completing Epics
----------------

An epic may be marked as “done” when:

#. It contains at least one completed story;
#. There are no more incomplete stories defined within it;
#. There are no plans to add more stories;
#. (If applicable, i.e. it is not a :ref:`bucket <sec-bucket>`) its concrete
   deliverable has been achieved.

Note that it is not permitted to close an epic without defining at least one
story within it. Empty epics can never be completed.

When an epic is marked as complete, :ref:`all of its value is earned
<sec-cycle-value>`.

.. _sec-bugs:

Handling Bugs & Emergent Work
-----------------------------

Receiving Bug Reports
^^^^^^^^^^^^^^^^^^^^^

Members of the project who have access to JIRA may report bugs or make feature
requests directly using JIRA. As discussed under :ref:`sec-jira-maintenance`,
technical managers should regularly monitor JIRA for relevant tickets and
ensure they are handled appropriately.

Our code repositories are exposed to the world in general through `GitHub`_.
Each repository on GitHub has a bug tracker associated with it. Members of the
public may report issues or make requests on the GitHub trackers. Per the
`Developer Workflow`_, all new work must be associated with a JIRA ticket
number before it can be committed to the repository. It is therefore the
responsibility of technical managers to file a JIRA ticket corresponding to
the GitHub ticket, to keep them synchronized with relevant information, and to
ensure that the GitHub ticket is closed when the issue is resolved in JIRA.

The GitHub issue trackers are, in some sense, not a core part of our workflow,
but they are fundamental to community expectations of how they can interact
with the project. Ensure that issues reported on GitHub are serviced promptly.

In some cases, the technical manager responsible for a given repository is
obvious, and they can be expected to take the lead on handling tickets.
Often, this is not the case: repositories regularly span team boundaries.
Work together to ensure that all tickets are handled.

.. _GitHub: https://github.com/lsst/
.. _Developer Workflow: https://developer.lsst.io/processes/workflow.html

Issue Types
^^^^^^^^^^^

We have previously referred to day-to-day work being described by means of
stories. However, JIRA provides us with two additional issue types: “bug” and
“improvement”. Per :jira:`RFC-43`, the semantics of the various issue types
are:

- A story is the result of breaking down an epic into workable units;
- A bug describes a fault or error in code which has already been accepted to
  master;
- An improvement describes a feature request or enhancement which has not
  been derived by breaking down the long term plan (i.e., it is an ad-hoc
  developer or user request).

The three issue types are functionally equivalent: these semantic distinctions
are for convenience only, and are not rigorously enforced.

In particular, note that all issue types are equivalent in terms of the data
which is loaded to :term:`PMCS`: it makes no distinction between them. Marking
a bug or improvement as done has exactly the same impact on the global earned
value state as would completing an equivalent story.

Scheduling
^^^^^^^^^^

In some cases, a ticket may describe emergent work which must be immediately
by adding it to a :ref:`bucket epic <sec-bucket>`. In other cases, it can be
deferred to a later cycle, or, after appropriate discussion, may be regarded
as inappropriate (and can be tagged as Invalid or Won't Fix). This is a
management decision. When closing a ticket as inappropriate, please take a
moment to describe why—the individual who reported it will appreciate an
explanation of why it has been rejected, and it will serve as a useful
reference the next time somebody suggests the same thing.

A special case of inappropriate tickets are those that duplicate work which
has already been described elsewhere. Please close these as Invalid, and add a
JIRA link of type "duplicates" to the original ticket.

Relationship to Earned Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We adopt the position that bugs are a natural part of the software lifecycle,
and hence addressing them at an appropriate level earns value in the same way
as new software development. That is, SPs earned by working on bugs and
completing bucket epics contribute to earned value in the same way as other
work.

However, bugs do serve as an bellwether for software quality issues. It would
obviously be inappropriate—and a severe source of schedule risk—for the value
earned from addressing bugs in existing software to dominate the productivity
of the team at the expense of new development. We expect that no more than
around 30% of schedulable developer time will be dedicated addressing bugs and
performing maintenance: any more than this must be carefully justified.

.. _sec-cycle-value:

Earning Value
-------------

The basic procedure for earning value during the cycle is akin to that
:ref:`discussed earlier <sec-long-term-value>` for long term planning.

In short, :ref:`as we have seen <sec-sps-to-bcws>`, the :term:`BCWS` for a
particular epic is defined by its *estimated* (i.e. attached to the epic
before work commences) SP total and its staff assignment. When :ref:`an epic
is marked as complete <sec-epic-done>`, this is the value that is earned.

The :term:`BCWP` for an epic is calculated based on the fractional
completeness of an epic. That is, if an epic has a total SP count of ``X``,
and the total of stories marked as complete within it is ``Y``, then ``BCWP =
BCWS * Y / X``.

Be aware that stories that marked as “invalid” or “won't fix” in JIRA are not
included in this calculation: they earn no value.

:ref:`As we have seen <sec-defining-stories>`, it is not required that the
total SPs of all the stories contained within an epic (the “planned SPs”) is
equal to the total SP estimate of the epic itself (“estimated SPs”). Further,
it is permitted to add stories to (or, indeed, remove stories from) the epic
during the cycle. In these cases, we hold to two basic tenets:

#. No epic can ever be more than 100% complete;
#. Completeness cannot decrease. That is, if an epic has been registered as
   90% complete, adding more stories cannot make it *less* complete than
   before.

In order to meet these criteria, the relative weights of stories will be
automatically adjusted on ingest to the :term:`PMCS`. The detailed algorithm
by which this adjustment is made is not publicly documented.

.. _sec-jira-maintenance:

JIRA Maintenance
----------------

At any time, new tickets may be added to JIRA by team members. Please remind
your team of the best practice in this respect (:jira:`RFC-147`). It is the
responsibility of technical managers to ensure that new tickets are handled
appropriately, updating the schedule to include them where necessary. It is
required that the ``Team`` field be set to the appropriate team
(:jira:`RFC-145`). Please regularly monitor JIRA for incomplete tickets and
update them appropriately. Where tickets describe bugs or other urgent
emergent work which cannot be deferred, refer to :ref:`sec-bugs`.

Coordination Standup
--------------------

.. note::

   The meeting URL is not included here since this note is publicly available.
   Contact the Project Manager for details.

The technical managers meet with the :ref:`Project Manager <sec-contacts>` and
interested others (it is not a closed meeting) twice every week. This is a
forum to discuss general project management issues, but, in particular, to
resolve issues which cut across team boundaries and are relevant for the
ongoing sprint.

Meetings take place using `Google Hangouts`_ at a pre-arranged URL. Meetings
take place at 11:00 (11 a.m.) Project (Pacific) Time on Tuesdays and Fridays.

.. _Google Hangouts: https://hangouts.google.com/

.. _sec-monthly-narrative:

Monthly Progress Narratives
---------------------------

Every calendar month, each technical manager is required to support the
Project Manager with a report on the activities of their group. This report
should be generally submitted no later than tenth of the month (refer to the
:ref:`sec-monthly-cycle`), but this may be moved earlier on occasion. You are
encouraged to submit your report as early in the month as possible.

Submit your report by editing the `template for the appropriate month`_ on
Google Docs. You need to fill in all the sections with your name attached;
when complete, remove your name. Provide a brief (one or two sentences) high
level summary, a per-WBS breakdown of work over the month being reported on
and plans for the upcoming month, as well as describing any recruitment
activities (positions opened, interviews conducted, appointments made, etc).
Refer to previous reports for examples of the style used (but note that they
are not not always consistent).

.. _template for the appropriate month: https://drive.google.com/drive/u/0/folders/0BxgFbTQURmr6TUJleXZaY2ZNcEE

.. _sec-actuals:

Reporting Actuals
=================

In order to comply with the :ref:`earned value management system <sec-evms>`,
it is necessary to track the actual cost of work being performed (the
“actuals”) in each leaf element of the WBS. That is, whenever an invoice is
issue from a subcontracting institution to AURA, it must be broken down into
dollar charges against individual WBS elements.

Some institutions rigorously track how staff are spending their time (e.g. by
filling in timesheets), and may directly make that information available to
AURA as part of the invoicing process. In this case, the technical manager
need take no further action.

Other institutions do not rigorously check staff activity and/or do not supply
this information to AURA when invoicing. In this case, the technical manager
is responsible for breaking down the invoice by WBS and forwarding that to the
relevant AURA contracts officer (check with the :ref:`project manager
<sec-contacts>` if you are unsure who that is). Note that, since
:ref:`story points reflect estimated, not actual, time spent on work
<sec-sprinting>`, it is *not* appropriate to simply allocate actual costs
based on SP totals.

A typical invoice breakout should be supplied in a spreadsheet similar to that
shown in :numref:`tab-invoice`.

.. _tab-invoice:

.. table:: Example invoice breakout.

   +--------------------------+-----------+------------+-------------+------------+-----------+---------+-----------+-----------+-----------+------------+
   | Invoice Voucher          | Salary    | Fringe xx% | Materials & |  F & A yy% | Total     | WBS     | 02C.0N.00 | 02C.0N.01 | 02C.0N.02 | TOTAL      |
   |                          |           |            | Services    |            |           |         |           |           |           |            |
   +==========================+===========+============+=============+============+===========+=========+===========+===========+===========+============+
   | Invoice Date YYYY-MM-DD  |           |            |             |            |           | ACCOUNT | KLM20N00A | KLM20N01A | KLM20N02A |            |
   +--------------------------+-----------+------------+-------------+------------+-----------+---------+-----------+-----------+-----------+------------+
   | Invoice Period           | $ABCDE.FG |  $HIJKL.MN |   $OPQRS.TU |  $VWXYZ.AB | $CDEFG.HI | AMOUNT  | $12345.67 | $89012.34 | $56789.01 | $158147.02 |
   | YYYY-MM-DD -- YYYY-MM-DD |           |            |             |            |           |         |           |           |           |            |
   +--------------------------+-----------+------------+-------------+------------+-----------+---------+-----------+-----------+-----------+------------+

Note that when reporting actuals at this level it is not required to provide a
mapping from dollar values to individuals who did the work. However, it is
important to note that, should the Project be audited in the future, it is
perfectly possible that they will wish to examine such a mapping. You should
therefore keep records which will enable you to provide it upon request.

.. _sec-monthly-cycle:

Standard Reporting Cycle
========================

- During the first week of the calendar month, data from JIRA together with
  actual costs (labor charges, etc) are ingested to the :term:`PMCS` system.
  This indicates the progress of all activities and shows any Earned Value
  variances. This information is made available to technical managers through
  :term:`eCAM`.
- During the second week of the calendar month:

   - :ref:`sec-variance-narrative`, where necessary, must be submitted through
     eCAM.
   - :ref:`sec-monthly-narrative` must be submitted through Google Docs by the
     tenth day of the month.
- The DM Project Manager assembles extended and summary reports, based on the
  reports received from the institutions. The extended report is periodically
  examined by Federal auditors, while the summary report is provided to senior
  management and the :term:`AMCL` for review.

Staffing Changes
================

In addition to onboarding procedures at your local institution, please be
aware of

- The LSST `New Employee Onboarding`_ material, and
- The DM `Developer Onboarding Checklist`_

and direct new recruits to them when they join your team.

We maintain a `spreadsheet`_ listing all members of the DM team. Ensure it is
kept up to date with the current and projected staffing within your team.

.. _New Employee Onboarding: https://project.lsst.org/onboarding
.. _Developer Onboarding Checklist: https://developer.lsst.io/getting-started/onboarding.html
.. _spreadsheet: https://docs.google.com/spreadsheets/d/1G9KXBJJHfWkVDQeApfXaN_nZjD_YUJlHiEDOzhTy-0c/edit?usp=drive_web

Glossary
========

.. glossary::
   :sorted:

   ACWP
      Actual Cost of Work Performed (often referred to as “actuals”).

   AMCL
      AURA Management Committee for LSST.

   BCWP
      Budgeted Cost of Work Performed.

   BCWS
      Budgeted Cost of Work Scheduled.

   Budgeted (labor) unit
      An hour of work.

   CAM
      Control Account Manager. A CAM is responsible for the scope, schedule
      and budget for one or more :term:`control account`\s.

   CCB
      Change Control Board. All changes to the baselined plan must be approved
      by the CCB. See :lpm:`19` for details.

   Control Account
      An intersection point between the :term:`WBS` and the :term:`OBS`. For
      example, work performed at IPAC (1.03) on the Science User Interface
      (1.02C.05) is managed by a single control account.

   CPI
       Cost Performance Index. Defined as :term:`BCWP`\/:term:`ACWP`.

   CV
      Cost Variance. Defined as :term:`BCWP`\-:term:`ACWP`.

   Cycle
      The time period over which detailed, short-term plans are defined and
      executed. Normally, cycles run for six months, and culminate in a new
      release of the LSST Software Stack, however this need not always be the
      case.

   eCAM
      The `eCAM Notebook`_, a tool which reports information from the
      :term:`PMCS`. It provides a convenient view of the current status of the
      project in terms of :term:`EVMS`.

   Element
      A node in the hierarchical project :term:`WBS`.

   Epic
      A self contained work with a concrete deliverable which my be scheduled
      to take place with a single :term:`cycle` and :term:`WBS`
      :term:`element`.

   EVMS
      Earned Value Management System. See the brief description :ref:`above
      <sec-evms>`, or refer to formal training.

   JIRA
      Issue and project tracking software produced by `Atlassian`_. `LSST's
      JIRA`_ is a core interface between technical managers, their teams, and
      the :term:`PMCS`.

   LCR
      LSST Change Request. It is necessary to submit a change request to alter
      any “baselined” aspect of the project. This includes, for example,
      altering change controlled plans, or epics that have been loaded to PMCS.

   LOE
      Level of Effort. LOE work is that which does not correspond to a
      specific deliverable. A detailed definition is provided in :ldm:`472`;
      see also the discussion :ref:`above <sec-loe>`.

   MREFC
      Major Research Equipment and Facilities Construction. The terms under
      which LSST's NSF funding has been issued; we are required to strictly
      adhere to these.

   NSF
      National Science Foundation.

   OBS
      Organizational Breakdown Structure; see the definition :ref:`above
      <sec-obs>`.

   Risk
      Risks are (per ISO 31000) “the effect of uncertainty upon objectives”.
      For the purposes of this document, that corresponds to the impact of
      unplanned or unpredictable events upon the cost or schedule of the
      Project. The Project maintains a register of risks, which includes
      probability estimates and possible mitigations.

   PMCS
      Project Management Control System. The PMCS is not a single piece of
      software, but rather an interlocking suite of tools. In general, the CAM
      need not interact with PMCS directly, but only through the eCAM and JIRA
      tools: it is safe to treat PMCS as a “black box”. Occasionally,
      individual PMCS components such as Primavera or Deltek Cobra escape this
      abstraction and appear in documentation.

   Resource Loading
      Assigning particular resources (in software development, almost always
      staffing) to particular tasks. A “resource loaded plan” provides a
      mapping of resources to the plan throughout execution.

   SP
      Story Point. Used to estimate the duration of tasks in JIRA. One SP is
      equivalent to 4 hours of uninterrupted effort by a competent developer.

   SPI
       Schedule Performance Index. Defined as :term:`BCWP`\/:term:`BCWS`.

   Sprint
      A defined period of work for a particular team. Typically, sprints are
      one calendar month long, but this is not required.

   Story
      A JIRA issue type describing a scheduled, self-contained task worked as
      part of an epic. Typically, stories are appropriate for work worth
      between a fraction of a :term:`SP` and 10 SPs; beyond that, the work is
      insufficiently fine-grained to schedule as a story. While fractional SPs
      are fine, all stories involve work, so the SP total of an in progress or
      completed story should not be 0.

   SV
      Schedule Variance. Defined as :term:`BCWP`\-:term:`BCWS`.

   Timebox
      A limited time period assigned to a piece of work or other activity.
      Useful in scheduling work which is not otherwise easily limited in
      scope, for example research projects or servicing user requests.

   WBS
      Work Breakdown Structure; see the discussion :ref:`above <sec-wbs>`.

.. _eCAM Notebook: https://msweb.lsstcorp.org/eCAM/
.. _Atlassian: http://www.atlassian.com/
.. _LSST's JIRA: https://jira.lsstcorp.org/
