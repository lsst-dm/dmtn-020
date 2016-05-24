.. vim: ts=3:sts=3

:tocdepth: 1

This document provides an informal guide to the everyday mechanisms
underpinning LSST Data Management's approach to project management. It is
intended to be read in conjunction with :ldm:`465`, which provides a formal
description of the project management process and requirements.

Introduction
============

Technical Managers
==================

This guide is primarily aimed at the LSST DM technical managers. Technical
managers report directly to the DM Project Manager. Per :ldm:`465`, they are
expected to:

- Assemble the team capable of delivering work scoped through the WBS on-time
  and within budget. Provide daily technical management and leadership for the
  team, monitor and optimize team performance.

- Work closely with the DM Project Manager on defining short and long-term
  plan and schedule for their teams. Direct the execution of their teams's
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
======== ========================================= =======================

These subdivisions are referred to as the *third level WBS*. Often, they are
quoted without the leading “1” (e.g. “02C.01”), but, even in this form, they
are referred to as “third level”. Further subdivisions beneath the third level
are common, and depend on the requirements of the particular deliverable.
Nodes in the WBS tree are referred to as :term:`element`\s.

.. _sec-obs:

Organization Breakdown Structure
--------------------------------

In parallel with the WBS, we have an :term:`OBS`, which assigns each
institution involved in the project a unique numeric identifier. Those
directly relevant to DM are:

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
within DM, a single CAM is resposible for the whole of a third level WBS. That
is, the manager at the lead institution for a particular component is
responsible for all work performed on that WBS element, even if that work is
performed at another institution.

.. _sec-evms:

Earned Value
============

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
:term:`SV` (defined as BCWP-BCWS; a negative value means that less of the
system has been delivered to date than planned) and :term:`CV` (defined as
BCWP-ACWP; a negative value means that the work delivered to date has been
more expensive than predicted). Related quantities, :term:`SPI` and
:term:`CPI`, express the same information as ratios rather than sums. In
general, we strive to achieve variances of near zero: even a positive variance
(corresponding being ahead of schedule or being cheaper than expected) is
indicative of an inaccurate plan.

All of these indices can be applied to any WBS element within the project.
Thus, we can talk about value earned across the whole of DM (1.02C) or on a
very specific component (say, the User Workspace Toolkit, 1.02C.05.05).

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

:ldm:`465` provides a detailed definition of the types of work it is
permissible to regard as LOE. In general, we strive to minimize the fraction
of our effort which is devoted to LOE activities and favour those which are
more directly accountable.

The assumption encoded in :ldm:`465` is that developers will spent 30% of
their time on LOE type activities, and the remaining 70% of their effort is
tracked against concrete deliverables.

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
<sec-contacts>` if you are unsure who that is).

A typical invoice breakout should be supplied in a spreadsheet in the
following format:

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

Note that when loading the plan at the start of a cycle (as described
:ref:`here <sec-cycle-plan>`), you are expected to provide the names of the
individuals who will be carrying out the work. It is not, in general,
appropriate to charge for labor from individuals who have not been named in
this way, even if the total sum comes in below the budgeted amount specified
in your contract. In some special cases (e.g. temporary work carried out by
summer students) it may be possible to make an exception: please discuss this
with the :ref:`project manager <sec-contacts>` on a case-by-case basis.

.. _sec-cycle-plan:

Cycle Level Planning
====================



Important Documents
===================

Be aware of prefixes: “LDM-” documents refer specificially to the Data
Management subsystem, “LSE-” to Systems Engineering, “LPM-” to Project
Management.

:ldm:`465`
   *LSST DM Project Management and Tools*. The formal, high-level document
   which defines the project management process used by LSST DM. The present
   document may be thought of as a guide to applying the principles defined
   in :ldm:`465` in practice.

:lpm:`43`, :lpm:`44`
   *WBS Structure* and *WBS Dictionary*, respectively. The former shows the
   overall work breakdown structure for the whole project.

:lpm:`98`
   *LSST Project Controls System Description*. Describes and defines the
   components of the :term:`PMCS` used to manage and report on the overall
   LSST Project.

.. _sec-contacts:

Useful Contacts
===============

The LSST DM Project Manager is Jacek Becla. He is the first point of contact
for all issues regarding project management within DM.

The LSST Project Controls Specialist is Kevin Long. He is responsible for the
:term:`PMCS` and, in particular, for ensuring that DM properly complies with
our earned value management requirements. He is the first point of contact for
all questions about the PMCS system.

Glossary
========

.. glossary::
   :sorted:

   ACWP
      Actual Cost of Work Performed (often referred to as “actuals”).

   BCWP
      Budgeted Cost of Work Performed.

   BCWS
      Budgeted Cost of Work Scheduled.

   Budgeted units
      Hours.

      .. todo::

         Total working hours, or applied to story points? Check!

   CAM
      Control Account Manager. A CAM is responsible for the scope, schedule
      and budget for one or more :term:`control account`\s.

   Control Account
      An intersection point between the :term:`WBS` and the :term:`OBS`. For
      example, work performed at IPAC (1.03) on the Science User Interface
      (1.02C.05) is managed by a single control account.

   CPI
       Cost Performance Index. Defined as :term:`BCWP`\/:term:`ACWP`.

   CV
      Cost Variance. Defined as :term:`BCWP`\-:term:`ACWP`.

   eCAM
      The eCAM Notebook, a tool which reports information from the
      :term:`PMCS`. It provides a convenient view of the current status of the
      project in terms of :term:`EVMS`.

   Element
      A node in the hierarchical project :term:`WBS`.

   EVMS
      Earned Value Management System. See the brief description :ref:`above
      <sec-evms>`, or refer to formal training.

   LCR
      LSST Change Request. It is necessary to submit a change request to alter
      any “baselined” aspect of the project. This includes, for example,
      altering change controlled plans, or epics that have been loaded to PMCS.

   LOE
      Level of Effort. LOE work is that which does not correspond to a
      specific deliverable. A detailed definition is provided in :ldm:`465`;
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

   PMCS
      Project Management Control System. The PMCS is not a single piece of
      software, but rather an interlocking suite of tools. In general, the CAM
      need not interact with PMCS directly, but only through the eCAM and JIRA
      tools: it is safe to treat PMCS as a “black box”. Occasionally,
      individual PMCS components such as Primavera or Deltek Cobra escape this
      abstraction and appear in documentation.

   SPI
       Schedule Performance Index. Defined as :term:`BCWP`\/:term:`BCWS`.

   SV
      Schedule Variance. Defined as :term:`BCWP`\-:term:`BCWS`.

   WBS
      Work Breakdown Structure; see the discussion :ref:`above <sec-wbs>`.

Recruiting new staff
====================


