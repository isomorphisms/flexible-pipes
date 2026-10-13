# Venn movie: derive the picture and every fraction from one model

Status: replacement design, not an implemented or type-checked rewrite.
Continue the existing script and PR #104, “Add reproducible animated college/job
Venn pipeline”. Do not create another movie implementation or send source ZIPs.
The current source at f6c2ebc69b37dc63b12848d907205c64fbb2e40b still contains
separate handwritten percentage formulas, footer labels, and mask operations.
Its successful tests do not establish the dependent guarantees below.

Human requirement: “Maybe we need to redo this movie with dependent types.
You should know all these fractions programmatically and automatically.”

## The defect is semantic duplication, not difficult division

A model should choose the intended events once. It should not subsequently
choose a numerator, denominator, population label, region mask, and output
receipt independently. Patching each mistaken label and adding a test for that
label leaves the upstream generator defect in place.

Automatic calculation requires a measured set algebra. Dependent types add
machine-checked relationships between a query and its outputs; they are not
required merely to divide two numbers. A Python dataclass, JSON schema, renamed
file, or finite collection of runtime tests must not be called a dependent-type
proof.

## Mathematical source of truth

Use an explicitly declared universe U, college predicate C, and good-job
predicate G. Under the user's exhaustive job classification,

    bad job or no job ≝ U ∖ G

This includes people outside both C and G. It is not C ∖ G. A vocabulary alias
for the complement must be attached to that expression, not to a freely chosen
region. If the input has unknown job status, resolve or report it explicitly;
do not silently equate missing classification with a bad job or no job.

For the two predicates, generate the four disjoint cells mechanically:

    a ≝ μ(C ∩ G)
    b ≝ μ(C ∩ Gᶜ)
    c ≝ μ(Cᶜ ∩ G)
    d ≝ μ(Cᶜ ∩ Gᶜ)

The nonnegative cell measures determine every event's measure by addition.
Do not separately store totals that can disagree with those sums:

    μ(U)       ≝ a + b + c + d
    μ(C)       ≝ a + b
    μ(G)       ≝ a + c
    μ(Gᶜ)      ≝ b + d
    μ(C ∪ G)   ≝ a + b + c
    μ(Cᶜ ∩ Gᶜ) ≝ d

For a finite population, count membership. For a weighted schematic, use exact
nonnegative rational weights. These are distinct from raster pixel area. Any
adapter preserving the existing area-based example must declare that its
inputs are schematic area weights, not measured numbers of people.

## One generic conditional query

The only public percentage operation is:

    percentage(event A, among B, in frame t)
        ≝ 100 × μₜ(A ∩ B) ÷ μₜ(B)

The operation constructs A ∩ B itself. Callers cannot supply an independent
numerator. The requested counters are two instances of that same operation:

    percentage(G, among C)  → 100 × a ÷ (a + b)
    percentage(C, among G)  → 100 × a ÷ (a + c)

The definition, not a case-specific prompt or arithmetic branch, also gives
all other queries, including complements, unions, and differences. Two Boolean
predicates generate 16 events and 256 ordered event/conditioning-event pairs.
Empty conditioning populations produce an explicit undefined result, not 0%,
NaN hidden by formatting, or an arbitrary substitute denominator.

Generate the human-readable population/event label and symbolic fraction from
the same query. Atomic vocabulary is declared once. Compound labels are
derived from the expression, with a symbolic fallback when prose is ambiguous.
The layout layer may wrap or position text, but it may not replace its meaning.

## Dependent interface: specification, not checked language syntax

The intended semantic relationships can be expressed schematically as:

    Region U
    PopulationFrame U
    Measure frame region unit
    Percentage frame event conditioning_population

A Percentage value must contain, or be obtained by a constructor establishing:

    numerator   = μ_frame(event ∩ conditioning_population)
    denominator = μ_frame(conditioning_population)
    denominator > 0
    0 ≤ numerator ≤ denominator

The indices bind the universe, exact frame, event, and conditioning population.
The numerator and denominator cannot come from different frames, populations,
or units. A fraction about G among C is not interchangeable with a fraction
about C among G, even when a particular example gives equal numerical values.
Constructors and the renderer's query-to-label binding must prevent bypasses.

Do not introduce a bag of unrestricted number/string fields beside the typed
core. Checked semantics must determine the actual emitted data consumed by the
renderer, not merely verify a parallel example that the renderer can ignore.
Retain source/query/frame identity across any serialization boundary and
validate decoded values before constructing checked objects.

Target the user's Idriç semantic layer, with explicit compatibility boundaries
where needed. The canonical repository is isomorphisms/Idric, repository ID
1335092603, default branch Idriç. Follow its STYLE.md; the type sketch above is
not permission to rename ordinary Idris source or claim compiler acceptance.
Establish the actual pinned checker/runtime and required backend capability
before calling the replacement implemented. Do not expand the existing
Python-family migration debt into a new first-party framework.

## Animation is also a mathematical operation

The current expansion control b/a is not either footer percentage. Preserve
that distinction. Growing college membership outside G means increasing b.
With a and c fixed, the first requested percentage decreases and the second
stays constant. No special animation rule for either displayed number is
needed; reevaluate the same queries in each frame.

If the population U is fixed, b cannot simply appear from nowhere: d decreases
by the same amount, until exhausted. If U grows instead, that is a different
explicit scenario. Do not let canvas dimensions decide the population model.

If the intent is that college membership only expands, require Cₜ ⊆ Cₜ₊₁.
Keeping the intersection's AREA constant does not keep its MEMBERSHIP constant.
Sliding circles to preserve a lens area can change which points belong to C.
The layout must not silently substitute equal area for this stronger condition.

## Drawing is a downstream representation

One event expression must drive its mask, fill, legend, counted population, and
query participation. U ∖ G is rendered by the generic complement operation,
not a hand-selected crescent. Geometry is chosen to represent the model's
measures; the geometry does not invent the model's statistics.

Exact proportionality, fixed overlap, monotone inclusion, round circles, and a
fixed viewport are separate constraints. Some combinations need noncircular
boundaries or an explicitly approximate area layout. Report infeasibility or
use an allowed representation rather than changing populations to make circles
fit. A dependent proof about sets does not prove the pixel renderer or encoder
correct. Check their actual outputs independently with stated numerical and
raster tolerances.

## Acceptance and ownership

Extend the existing FP path to conceptually separate:

    checked model → evaluated frame queries → layout → render → output checks

Reuse the existing script/PR and keep any reusable enforcement in ai-ci.
Tests must include an independent finite-population oracle with asymmetric
cell counts, all events and conditionals, empty populations, mixed frames,
wrong universes/units, complements, partition sums, scaling, and animation
invariants. Compile-negative cases must attempt swapped semantic indices and
unproven denominators. Merely failing for an unrelated syntax error is not
successful rejection evidence.

Include a fixture where P(G|C) equals P(C|G) numerically: swapped query meaning
must still be rejected. Include a failure where correct metadata accompanies
incorrect visible text/masks: self-reported receipts are not enough.

Preserve the earlier wrong count ratio and college-only complement as
regressions, but test the generic mechanism rather than adding more special
cases for this one movie. Bind every acceptance result to its exact source,
model, selected queries, frame inputs, renderer, and emitted artifacts.

An accepted formal model does not establish that empirical input rates are
true, nor that the human's intended query was selected correctly. Those remain
input/intent obligations. The existing movie is schematic; do not promote its
37.9% or any other chosen percentage to an employment statistic.
