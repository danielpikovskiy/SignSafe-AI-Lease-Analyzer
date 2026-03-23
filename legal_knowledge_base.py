# legal_knowledge_base.py

# ============================================================
# CALIFORNIA (Los Angeles focus)
# ============================================================
CALIFORNIA_VIOLATIONS = {
    "excessive_security_deposit": {
        "violation_name": "Excessive Security Deposit",
        "limit": "2x monthly rent (unfurnished) or 3x monthly rent (furnished)",
        "statute": "California Civil Code Section 1950.5",
        "statute_text": "Security deposits cannot exceed two months' rent for unfurnished units or three months' rent for furnished units.",
        "severity": "HIGH",
        "category": "Financial",
        "trigger_keywords": ["security deposit", "deposit amount", "initial deposit"],
        "explanation": "California law strictly limits security deposits. Landlords who charge excessive deposits must refund the excess amount immediately.",
        "tenant_remedy": "Demand immediate refund of excess amount. If landlord refuses, tenant can sue in small claims court for the excess plus potential damages.",
        "compliant_clause_example": "Security deposit shall not exceed two times the monthly rent for this unfurnished unit, in accordance with California Civil Code Section 1950.5."
    },
    "missing_habitability_warranty": {
        "violation_name": "Waiver of Implied Warranty of Habitability",
        "requirement": "Landlord must maintain premises in habitable condition",
        "statute": "California Civil Code Section 1941",
        "statute_text": "The lessor of a building intended for the occupation of human beings must put it in a condition fit for such occupation and repair all subsequent dilapidations thereof.",
        "severity": "HIGH",
        "category": "Health & Safety",
        "trigger_keywords": ["as-is", "waives habitability", "accepts condition", "no warranty", "tenant responsible for all repairs"],
        "explanation": "Landlords cannot require tenants to waive their right to a habitable dwelling. Any clause attempting this is void and unenforceable under California law.",
        "tenant_remedy": "This clause is automatically void. Tenant retains all habitability rights regardless of lease language.",
        "compliant_clause_example": "Landlord shall maintain the premises in compliance with all applicable building, housing, and health codes, and in a habitable condition as required by California Civil Code Section 1941."
    },
    "illegal_late_fees": {
        "violation_name": "Excessive or Unreasonable Late Fees",
        "limit": "Must be 'reasonable' - generally under 10% of monthly rent or $50-75",
        "statute": "California Civil Code Section 1671",
        "statute_text": "Late fees must be a reasonable estimate of damages and cannot function as penalties. Courts generally find fees over 10% of rent or that compound daily to be unreasonable.",
        "severity": "MEDIUM",
        "category": "Financial",
        "trigger_keywords": ["late fee", "late charge", "penalty", "per day", "daily charge"],
        "explanation": "California prohibits penalty clauses in contracts. Late fees must reasonably reflect the landlord's actual administrative costs, not punish the tenant.",
        "tenant_remedy": "Refuse to pay excessive portion of late fee. If sued, argue fee is an unenforceable penalty under Civil Code 1671.",
        "compliant_clause_example": "If rent is not received within 5 days of due date, a late fee of $50 may be charged to cover administrative costs."
    },
    "security_deposit_return_violation": {
        "violation_name": "Improper Security Deposit Return Timeline",
        "requirement": "Must return deposit within 21 days with itemized statement",
        "statute": "California Civil Code Section 1950.5(g)",
        "statute_text": "The landlord shall, within 21 calendar days after the tenant has vacated the premises, furnish the tenant an itemized statement indicating the amount of any security deposit received and the disposition of such security deposit.",
        "severity": "MEDIUM",
        "category": "Financial",
        "trigger_keywords": ["deposit return", "within 30 days", "within 60 days", "reasonable time", "upon inspection"],
        "explanation": "California law mandates a strict 21-day deadline. Any lease provision extending this timeline is void and unenforceable.",
        "tenant_remedy": "If landlord misses 21-day deadline without good cause, tenant may be entitled to full deposit return plus bad faith damages up to 2x the deposit amount.",
        "compliant_clause_example": "Security deposit will be returned within 21 days of tenant vacating, along with an itemized statement of any deductions, as required by California Civil Code Section 1950.5."
    },
    "illegal_entry_provisions": {
        "violation_name": "Improper Entry Notice Requirements",
        "requirement": "24-hour advance written notice required for non-emergency entry",
        "statute": "California Civil Code Section 1954",
        "statute_text": "The landlord may enter only during normal business hours and only after giving reasonable notice (presumed to be 24 hours), except in emergency or when tenant consents at the time of entry.",
        "severity": "HIGH",
        "category": "Privacy Rights",
        "trigger_keywords": ["enter at any time", "without notice", "12 hour notice", "immediate access", "landlord may enter"],
        "explanation": "Tenants have a right to privacy and quiet enjoyment. Landlords cannot enter without 24-hour notice except in true emergencies.",
        "tenant_remedy": "Refuse entry if proper notice not given (except emergencies). Document violations and file complaint with local housing authority if pattern continues.",
        "compliant_clause_example": "Landlord may enter the premises only with 24-hour advance written notice during normal business hours, except in emergencies, as specified in California Civil Code Section 1954."
    },
    "waiver_of_repair_rights": {
        "violation_name": "Prohibited Waiver of Repair and Deduct Rights",
        "requirement": "Tenants cannot waive right to repair and deduct",
        "statute": "California Civil Code Section 1942.1",
        "statute_text": "If a landlord fails to maintain habitable premises after notice, tenant may have repairs made and deduct the cost from rent, up to one month's rent. This right cannot be waived.",
        "severity": "HIGH",
        "category": "Repair Rights",
        "trigger_keywords": ["may not make repairs", "cannot deduct", "waives repair rights", "no self-help", "prohibited from hiring"],
        "explanation": "California explicitly protects the tenant's right to repair and deduct. Any waiver of this right is void.",
        "tenant_remedy": "Clause is void. Tenant retains repair and deduct rights under Civil Code 1942.1 regardless of lease language.",
        "compliant_clause_example": "Tenant has the right to repair and deduct as provided by California Civil Code Section 1942.1 if landlord fails to make necessary repairs after proper notice."
    },
    "retaliatory_eviction_clause": {
        "violation_name": "Retaliatory Eviction or Threat Language",
        "protection": "Cannot retaliate against tenants exercising legal rights",
        "statute": "California Civil Code Section 1942.5",
        "statute_text": "It is unlawful for a landlord to increase rent, decrease services, cause a tenant to quit involuntarily, bring an action to recover possession, or threaten to do any of those acts, for retaliatory purposes.",
        "severity": "HIGH",
        "category": "Retaliation Protection",
        "trigger_keywords": ["complaints may result", "exercise of rights", "non-renewal if", "reporting violations", "contact authorities"],
        "explanation": "Landlords cannot threaten or take action against tenants who exercise their legal rights, such as filing complaints or requesting repairs.",
        "tenant_remedy": "Report retaliatory actions to local housing authority. If evicted in retaliation, tenant has strong defense in court and may recover damages.",
        "compliant_clause_example": "This lease shall not be construed to limit tenant's rights under California Civil Code Section 1942.5, including the right to make complaints to authorities without retaliation."
    },
    "missing_bedbug_disclosure": {
        "violation_name": "Missing Bedbug Disclosure",
        "requirement": "Must provide written bedbug information and disclosure",
        "statute": "California Civil Code Section 1954.602-605",
        "statute_text": "Landlords must provide tenants with written notice about bedbug identification, behavior, and treatment, along with disclosure of any known bedbug infestation in the unit within the past two years.",
        "severity": "MEDIUM",
        "category": "Required Disclosures",
        "trigger_keywords": ["bedbug", "bed bug", "pest disclosure"],
        "explanation": "California requires specific bedbug disclosures before signing a lease. Missing this disclosure violates state law.",
        "tenant_remedy": "Request disclosure immediately. If landlord knowingly concealed bedbug history, tenant may have grounds to break lease or seek damages.",
        "compliant_clause_example": "Landlord has provided tenant with the required bedbug disclosure and information sheet as mandated by California Civil Code Sections 1954.602-605. No bedbug infestations have been reported in this unit in the past two years."
    },
    "illegal_liquidated_damages": {
        "violation_name": "Unreasonable Early Termination Penalty",
        "rule": "Early termination fees must be reasonable estimate of damages",
        "statute": "California Civil Code Section 1671",
        "statute_text": "A liquidated damages provision is valid only if it represents a reasonable attempt to estimate actual damages and not a penalty. Requiring payment of all remaining rent is generally considered an unenforceable penalty.",
        "severity": "MEDIUM",
        "category": "Financial",
        "trigger_keywords": ["all remaining rent", "balance of lease", "liquidated damages", "early termination fee exceeds"],
        "explanation": "California law prohibits penalty clauses. Early termination fees must reasonably estimate actual damages (typically 1-2 months rent), not punish the tenant.",
        "tenant_remedy": "Challenge excessive fees as unenforceable penalties. Landlord has duty to mitigate damages by re-renting promptly.",
        "compliant_clause_example": "If tenant terminates lease early, tenant shall pay reasonable costs of re-renting (not to exceed two months' rent) to cover advertising, lost rent during vacancy, and administrative costs."
    },
    "missing_mold_disclosure": {
        "violation_name": "Missing Mold Disclosure",
        "requirement": "Must provide Mold Information Booklet",
        "statute": "California Health and Safety Code Section 26147",
        "statute_text": "Landlords must provide tenants with 'The Mold in Your Home' booklet published by the California Department of Public Health before or at the time of lease signing.",
        "severity": "LOW",
        "category": "Required Disclosures",
        "trigger_keywords": ["mold disclosure", "mold information", "health and safety booklet"],
        "explanation": "California requires landlords to provide educational materials about mold prevention and remediation.",
        "tenant_remedy": "Request the booklet from landlord. While violation doesn't void lease, it may support habitability claims if mold issues arise.",
        "compliant_clause_example": "Landlord has provided tenant with 'The Mold in Your Home' booklet as required by California Health and Safety Code Section 26147."
    },
    # LA-SPECIFIC
    "rent_control_violation": {
        "violation_name": "Rent Control Violation (RSO Properties)",
        "applicability": "Buildings built before October 1, 1978 in City of Los Angeles",
        "requirement": "Annual rent increases limited by LAHD formula (typically 3-8%)",
        "statute": "Los Angeles Municipal Code (LAMC) Section 151.00 et seq.",
        "statute_text": "The Rent Stabilization Ordinance (RSO) limits annual rent increases for qualifying units built before 10/1/1978. Increases cannot exceed the allowable amount set annually by the Los Angeles Housing Department.",
        "severity": "HIGH",
        "category": "LA Rent Control",
        "trigger_keywords": ["rent increase", "annual increase", "percentage increase", "adjusted annually"],
        "explanation": "In Los Angeles, many buildings are subject to LA's Rent Stabilization Ordinance. Landlords cannot increase rent beyond the allowable percentage set by LAHD each year.",
        "tenant_remedy": "File complaint with LA Housing Department. Excess increases are void and must be refunded. Tenants may also be entitled to damages.",
        "compliant_clause_example": "For RSO-covered units: Rent increases shall not exceed the maximum allowable amount established annually by the Los Angeles Housing Department under LAMC Section 151.00 et seq."
    },
    "just_cause_eviction_violation": {
        "violation_name": "Missing Just Cause Eviction Protections",
        "applicability": "RSO properties in Los Angeles",
        "requirement": "Can only evict for specific legal reasons",
        "statute": "Los Angeles Municipal Code Section 151.09",
        "statute_text": "Landlords of RSO units can only terminate tenancy for just cause, including: non-payment of rent, breach of lease, nuisance, illegal use, owner move-in, Ellis Act withdrawal, or substantial remodeling.",
        "severity": "HIGH",
        "category": "LA Eviction Protection",
        "trigger_keywords": ["terminate at will", "without cause", "month to month termination", "discretion to terminate"],
        "explanation": "In RSO units, landlords cannot terminate tenancies without one of the specific just causes enumerated in the law. 'No cause' evictions are illegal.",
        "tenant_remedy": "If evicted without just cause, tenant can challenge eviction in court. Landlord may owe tenant relocation fees and damages.",
        "compliant_clause_example": "For RSO-covered units: Landlord may only terminate this tenancy for just cause as defined in Los Angeles Municipal Code Section 151.09."
    },
    "missing_relocation_assistance": {
        "violation_name": "Missing Relocation Assistance Notice",
        "applicability": "Required for certain evictions in RSO units",
        "requirement": "Must pay relocation fees for no-fault evictions",
        "statute": "Los Angeles Municipal Code Section 151.09(C)",
        "statute_text": "For no-fault evictions (owner move-in, Ellis Act, major remodeling), landlord must pay relocation assistance ranging from $8,700-$21,500+ depending on tenant demographics and unit type.",
        "severity": "MEDIUM",
        "category": "LA Eviction Protection",
        "trigger_keywords": ["owner move-in", "substantial remodel", "demolition", "Ellis Act", "relocation"],
        "explanation": "When landlords evict tenants through no fault of the tenant in RSO units, they must pay substantial relocation fees set by the city.",
        "tenant_remedy": "If landlord attempts no-fault eviction without offering relocation assistance, eviction may be invalid. File complaint with LAHD.",
        "compliant_clause_example": "For RSO-covered units: If landlord terminates tenancy due to owner move-in, Ellis Act withdrawal, or substantial remodeling, landlord shall pay relocation assistance as required by LAMC Section 151.09(C)."
    },
    "missing_rso_notice": {
        "violation_name": "Missing Rent Stabilization Ordinance Notice",
        "applicability": "All RSO-covered units in Los Angeles",
        "requirement": "Must notify tenants if unit is RSO-covered",
        "statute": "Los Angeles Municipal Code Section 151.05",
        "statute_text": "Landlords must provide written notice to tenants informing them whether the unit is subject to the Rent Stabilization Ordinance, including LAHD contact information.",
        "severity": "MEDIUM",
        "category": "LA Required Disclosures",
        "trigger_keywords": ["rent stabilization", "RSO", "rent control notice", "LAHD"],
        "explanation": "Tenants have a right to know if their unit is protected under LA's rent control laws. Missing this notice violates city law.",
        "tenant_remedy": "Request notice from landlord. Contact LAHD at (866) 557-7368 to verify RSO status of your unit.",
        "compliant_clause_example": "NOTICE: This unit [IS / IS NOT] subject to the City of Los Angeles Rent Stabilization Ordinance. For more information, contact the Los Angeles Housing Department at (866) 557-7368."
    }
}


# ============================================================
# NEW YORK
# ============================================================
NEW_YORK_VIOLATIONS = {
    "excessive_security_deposit_ny": {
        "violation_name": "Excessive Security Deposit",
        "limit": "Maximum 1 month's rent for most rentals (Housing Stability and Tenant Protection Act 2019)",
        "statute": "New York General Obligations Law Section 7-108",
        "statute_text": "Security deposits for residential rentals are capped at one month's rent. Landlords must return deposits within 14 days of tenant vacating with an itemized statement.",
        "severity": "HIGH",
        "category": "Financial",
        "trigger_keywords": ["security deposit", "deposit amount", "initial deposit", "two months", "three months"],
        "explanation": "Since 2019, New York law caps security deposits at one month's rent for virtually all residential rentals. Charging more is illegal.",
        "tenant_remedy": "Demand refund of excess deposit immediately. File a complaint with the NY Division of Housing and Community Renewal (DHCR) or pursue in small claims court.",
        "compliant_clause_example": "Security deposit shall not exceed one month's rent, as required by New York General Obligations Law Section 7-108."
    },
    "missing_habitability_warranty_ny": {
        "violation_name": "Waiver of Warranty of Habitability",
        "requirement": "Landlord must maintain premises in habitable condition",
        "statute": "New York Real Property Law Section 235-b",
        "statute_text": "In every written or oral lease for residential premises, the landlord covenants and warrants that the premises are fit for human habitation. This warranty cannot be waived.",
        "severity": "HIGH",
        "category": "Health & Safety",
        "trigger_keywords": ["as-is", "accepts condition", "no warranty", "tenant responsible for all repairs", "waives habitability"],
        "explanation": "New York's implied warranty of habitability cannot be waived by any lease clause. Any attempt to do so is void.",
        "tenant_remedy": "Clause is void. Notify landlord in writing of any habitability issues and document all communications. May withhold rent or pursue rent reduction through DHCR.",
        "compliant_clause_example": "Landlord warrants that the premises are habitable and will remain so throughout the tenancy, as required by New York Real Property Law Section 235-b."
    },
    "illegal_entry_ny": {
        "violation_name": "Improper Entry Notice Requirements",
        "requirement": "Reasonable advance notice required; NYC requires written notice",
        "statute": "New York Real Property Law Section 235 / NYC Admin Code 27-2005",
        "statute_text": "Landlords must provide reasonable advance written notice before entering a tenant's unit, except in emergencies. Repeated unauthorized entry may constitute harassment.",
        "severity": "HIGH",
        "category": "Privacy Rights",
        "trigger_keywords": ["enter at any time", "without notice", "immediate access", "landlord may enter", "right of entry"],
        "explanation": "Tenants have a right to quiet enjoyment. Unauthorized entry or clauses allowing entry without notice violate New York law.",
        "tenant_remedy": "Document unauthorized entries. File a harassment complaint with NYC's Office to End Domestic and Gender-Based Violence or DHCR if pattern continues.",
        "compliant_clause_example": "Landlord shall provide reasonable advance written notice before entering the premises, except in emergencies, consistent with New York Real Property Law Section 235."
    },
    "rent_stabilization_ny": {
        "violation_name": "Rent Stabilization Violation (NYC)",
        "applicability": "Buildings with 6+ units built before 1974 in NYC",
        "requirement": "Annual increases limited by Rent Guidelines Board",
        "statute": "NYC Administrative Code Title 26 / Rent Stabilization Law",
        "statute_text": "Rent-stabilized units are subject to annual rent increase guidelines set by the NYC Rent Guidelines Board. Landlords cannot increase rent beyond the approved percentage without DHCR approval.",
        "severity": "HIGH",
        "category": "Rent Control",
        "trigger_keywords": ["rent increase", "annual increase", "percentage increase", "market rate", "adjusted annually"],
        "explanation": "If the unit is rent-stabilized, the landlord may only raise rent by the percentage allowed by the NYC Rent Guidelines Board each year.",
        "tenant_remedy": "File complaint with DHCR. Overcharges must be refunded and may result in treble damages for willful violations.",
        "compliant_clause_example": "For rent-stabilized units: Annual rent increases shall not exceed the guidelines established by the NYC Rent Guidelines Board for the applicable lease term."
    },
    "illegal_fees_ny": {
        "violation_name": "Illegal Fees and Charges",
        "requirement": "Landlords cannot charge application fees or most other fees",
        "statute": "New York General Obligations Law Section 7-108 / Housing Stability and Tenant Protection Act 2019",
        "statute_text": "Landlords may not charge fees for processing, reviewing, or accepting a rental application beyond actual costs, and cannot charge move-in fees, move-out fees, or other ancillary charges not permitted by law.",
        "severity": "MEDIUM",
        "category": "Financial",
        "trigger_keywords": ["application fee", "move-in fee", "administrative fee", "processing fee", "amenity fee", "pet fee"],
        "explanation": "New York's 2019 tenant protection law prohibits most ancillary fees that landlords previously charged.",
        "tenant_remedy": "Refuse to pay prohibited fees. File complaint with NY Attorney General's office. Landlords found in violation may be subject to penalties.",
        "compliant_clause_example": "No additional fees beyond rent and the permitted one-month security deposit shall be charged, in accordance with New York General Obligations Law Section 7-108."
    },
    "retaliation_ny": {
        "violation_name": "Retaliatory Eviction or Rent Increase",
        "protection": "Cannot retaliate against tenants exercising legal rights",
        "statute": "New York Real Property Law Section 223-b",
        "statute_text": "A landlord shall not serve a notice to quit, maintain a summary proceeding, or threaten to do so in retaliation for a tenant's good-faith complaint to a governmental authority or lawful exercise of tenant rights.",
        "severity": "HIGH",
        "category": "Retaliation Protection",
        "trigger_keywords": ["complaints may result", "non-renewal if", "reporting violations", "exercise of rights"],
        "explanation": "New York law prohibits landlords from retaliating against tenants who complain to authorities or exercise their legal rights.",
        "tenant_remedy": "Retaliation is a defense to eviction. Tenant may also bring an affirmative action for damages, attorney's fees, and injunctive relief.",
        "compliant_clause_example": "Landlord shall not retaliate against tenant for exercising any rights afforded by New York Real Property Law Section 223-b or other applicable law."
    },
    "deposit_return_ny": {
        "violation_name": "Improper Security Deposit Return Timeline",
        "requirement": "Must return deposit within 14 days with itemized statement",
        "statute": "New York General Obligations Law Section 7-108(e)",
        "statute_text": "Landlords must return the security deposit within 14 days of the tenant vacating, along with an itemized statement of any deductions. Failure to do so forfeits the right to any deductions.",
        "severity": "MEDIUM",
        "category": "Financial",
        "trigger_keywords": ["deposit return", "within 30 days", "within 60 days", "reasonable time", "upon inspection"],
        "explanation": "New York law requires return of the deposit within 14 days. Any lease clause extending this deadline is unenforceable.",
        "tenant_remedy": "If landlord fails to return deposit within 14 days, tenant is entitled to full deposit return regardless of any deductions.",
        "compliant_clause_example": "Security deposit shall be returned within 14 days of tenant vacating the premises, with an itemized statement of any deductions, per New York General Obligations Law Section 7-108(e)."
    }
}


# ============================================================
# TEXAS
# ============================================================
TEXAS_VIOLATIONS = {
    "deposit_return_tx": {
        "violation_name": "Improper Security Deposit Return Timeline",
        "requirement": "Must return deposit within 30 days of tenant vacating",
        "statute": "Texas Property Code Section 92.103",
        "statute_text": "A landlord shall refund a security deposit to the tenant on or before the 30th day after the date the tenant surrenders the premises. The landlord must provide an itemized list of deductions.",
        "severity": "HIGH",
        "category": "Financial",
        "trigger_keywords": ["deposit return", "within 60 days", "reasonable time", "upon inspection", "after surrender"],
        "explanation": "Texas law sets a strict 30-day deadline. Any lease clause extending the return timeline beyond 30 days is unenforceable.",
        "tenant_remedy": "If landlord fails to return deposit within 30 days, tenant may sue for 3x the deposit amount plus $100 and attorney's fees under Section 92.109.",
        "compliant_clause_example": "Security deposit will be returned within 30 days of tenant vacating, with an itemized written description of deductions, as required by Texas Property Code Section 92.103."
    },
    "habitability_tx": {
        "violation_name": "Failure to Maintain Habitable Conditions",
        "requirement": "Landlord must make repairs that materially affect health or safety",
        "statute": "Texas Property Code Section 92.052-92.061",
        "statute_text": "A landlord shall make a diligent effort to repair or remedy a condition that materially affects the physical health or safety of an ordinary tenant, if the tenant gives the landlord notice of the condition.",
        "severity": "HIGH",
        "category": "Health & Safety",
        "trigger_keywords": ["as-is", "accepts condition", "no warranty", "tenant responsible for all repairs", "waives rights"],
        "explanation": "Texas law requires landlords to repair conditions affecting health and safety. Clauses waiving this duty or making tenants responsible for all repairs may be unenforceable.",
        "tenant_remedy": "Give landlord written notice. If not repaired within a reasonable time, tenant may terminate lease, repair and deduct, or sue for damages.",
        "compliant_clause_example": "Landlord agrees to diligently repair conditions that materially affect the health or safety of tenants, as required by Texas Property Code Section 92.052."
    },
    "illegal_lockout_tx": {
        "violation_name": "Illegal Lockout or Utility Cutoff Provision",
        "requirement": "Landlord cannot lock out tenant or cut utilities as eviction method",
        "statute": "Texas Property Code Section 92.0081 / Section 92.008",
        "statute_text": "A landlord may not intentionally prevent a tenant from entering the leasehold premises or interrupt a utility service paid for by the tenant except by judicial process.",
        "severity": "HIGH",
        "category": "Tenant Protections",
        "trigger_keywords": ["lock out", "change locks", "interrupt utilities", "terminate utilities", "cut off"],
        "explanation": "Self-help eviction methods (lockouts, utility cutoffs) are illegal in Texas. Only a court can order a tenant removed.",
        "tenant_remedy": "Tenant may recover possession, actual damages, one month's rent plus $500, attorney's fees, and court costs if landlord uses self-help eviction.",
        "compliant_clause_example": "Landlord may not lock out tenant or interrupt utility services except through judicial process, as required by Texas Property Code Sections 92.0081 and 92.008."
    },
    "retaliation_tx": {
        "violation_name": "Retaliatory Conduct by Landlord",
        "protection": "Cannot retaliate against tenants exercising legal rights",
        "statute": "Texas Property Code Section 92.331",
        "statute_text": "A landlord may not retaliate against a tenant by increasing rent, decreasing services, or threatening to file or filing an eviction proceeding because the tenant complained in good faith, exercised a legal right, or organized a tenant association.",
        "severity": "HIGH",
        "category": "Retaliation Protection",
        "trigger_keywords": ["complaints may result", "non-renewal if", "reporting violations", "exercise of rights"],
        "explanation": "Texas law prohibits landlords from retaliating against tenants who make good-faith complaints or exercise their legal rights.",
        "tenant_remedy": "Retaliation is a defense to eviction. Tenant may also sue for one month's rent plus $500, actual damages, attorney's fees, and court costs.",
        "compliant_clause_example": "Landlord shall not retaliate against tenant for exercising any rights afforded by Texas Property Code Section 92.331 or other applicable law."
    },
    "illegal_waiver_tx": {
        "violation_name": "Illegal Waiver of Statutory Rights",
        "requirement": "Tenants cannot waive rights granted by Texas Property Code",
        "statute": "Texas Property Code Section 92.006",
        "statute_text": "A landlord and tenant may agree to a provision of a lease that is not prohibited by this subchapter or other applicable law. A lease provision that purports to waive a right or exempt a party from a liability or duty under this subchapter is void.",
        "severity": "HIGH",
        "category": "Tenant Protections",
        "trigger_keywords": ["waives all rights", "tenant waives", "agrees not to", "forfeits right", "waiver of claims"],
        "explanation": "Any lease clause that attempts to waive rights granted by the Texas Property Code is automatically void and unenforceable.",
        "tenant_remedy": "Clause is void by operation of law. Tenant retains all statutory rights regardless of any waiver language in the lease.",
        "compliant_clause_example": "Nothing in this lease shall be construed to waive tenant's rights under the Texas Property Code or other applicable law."
    },
    "late_fee_tx": {
        "violation_name": "Excessive or Improperly Structured Late Fee",
        "limit": "Cannot exceed 12% of monthly rent for properties with 4+ units; 10% for smaller properties",
        "statute": "Texas Property Code Section 92.019",
        "statute_text": "A landlord may not charge a late fee unless the rent is unpaid on or after the 2nd day after due date, and the fee cannot exceed 12% of rent for complexes with more than 4 units (10% for smaller).",
        "severity": "MEDIUM",
        "category": "Financial",
        "trigger_keywords": ["late fee", "late charge", "penalty", "per day", "grace period"],
        "explanation": "Texas caps late fees and requires a minimum 2-day grace period before any fee can be charged.",
        "tenant_remedy": "Refuse to pay late fees assessed before the 2-day grace period expires or that exceed the statutory cap.",
        "compliant_clause_example": "If rent remains unpaid after the 2nd day following the due date, a late fee not exceeding 12% of one month's rent may be assessed, per Texas Property Code Section 92.019."
    }
}


# ============================================================
# FLORIDA
# ============================================================
FLORIDA_VIOLATIONS = {
    "deposit_return_fl": {
        "violation_name": "Improper Security Deposit Return Timeline",
        "requirement": "Must return deposit within 15-60 days depending on circumstances",
        "statute": "Florida Statute Section 83.49",
        "statute_text": "If landlord claims no deductions, must return deposit within 15 days. If claiming deductions, must provide written notice within 30 days. Tenant has 15 days to object. Landlord must then return remaining balance within 30 days.",
        "severity": "HIGH",
        "category": "Financial",
        "trigger_keywords": ["deposit return", "within 90 days", "reasonable time", "upon inspection", "after surrender"],
        "explanation": "Florida has a specific multi-step process for deposit returns. Any lease clause modifying these timelines is unenforceable.",
        "tenant_remedy": "If landlord fails to follow proper procedures, tenant may be entitled to full deposit return plus attorney's fees.",
        "compliant_clause_example": "Security deposit will be returned within 15 days of tenant vacating (if no deductions), or landlord will provide written notice of intended deductions within 30 days, as required by Florida Statute Section 83.49."
    },
    "habitability_fl": {
        "violation_name": "Waiver of Warranty of Habitability",
        "requirement": "Landlord must maintain premises in habitable condition",
        "statute": "Florida Statute Section 83.51",
        "statute_text": "The landlord at all times during the tenancy shall maintain the premises in compliance with applicable building, housing, and health codes, and make necessary repairs to maintain the premises in a habitable condition.",
        "severity": "HIGH",
        "category": "Health & Safety",
        "trigger_keywords": ["as-is", "accepts condition", "no warranty", "tenant responsible for all repairs"],
        "explanation": "Florida landlords have a statutory duty to maintain habitable premises. Clauses attempting to waive this duty are void.",
        "tenant_remedy": "Give landlord 7 days written notice. If not repaired, tenant may withhold rent, terminate lease, or sue for damages.",
        "compliant_clause_example": "Landlord shall maintain the premises in compliance with applicable building, housing, and health codes as required by Florida Statute Section 83.51."
    },
    "illegal_entry_fl": {
        "violation_name": "Improper Entry Notice Requirements",
        "requirement": "12-hour advance notice required for non-emergency entry",
        "statute": "Florida Statute Section 83.53",
        "statute_text": "The landlord shall not abuse the right of access or use it to harass the tenant. The landlord shall give at least 12 hours notice before entry, and may only enter between 7:30 a.m. and 8:00 p.m.",
        "severity": "HIGH",
        "category": "Privacy Rights",
        "trigger_keywords": ["enter at any time", "without notice", "immediate access", "landlord may enter", "right of entry"],
        "explanation": "Florida requires at least 12 hours advance notice and restricts entry to between 7:30 AM and 8:00 PM, except in emergencies.",
        "tenant_remedy": "Refuse entry if proper notice not given. If landlord repeatedly enters without notice, tenant may terminate the lease.",
        "compliant_clause_example": "Landlord may enter the premises only with at least 12 hours advance notice between 7:30 a.m. and 8:00 p.m., except in emergencies, per Florida Statute Section 83.53."
    },
    "retaliation_fl": {
        "violation_name": "Retaliatory Conduct by Landlord",
        "protection": "Cannot retaliate against tenants exercising legal rights",
        "statute": "Florida Statute Section 83.64",
        "statute_text": "It is unlawful for a landlord to retaliate against a tenant by increasing rent, threatening to bring action for possession, or decreasing services because the tenant complained to a government agency or exercised a legal right.",
        "severity": "HIGH",
        "category": "Retaliation Protection",
        "trigger_keywords": ["complaints may result", "non-renewal if", "reporting violations", "exercise of rights"],
        "explanation": "Florida law prohibits landlords from retaliating against tenants who make good-faith complaints or exercise their legal rights.",
        "tenant_remedy": "Retaliation is a defense to eviction. Tenant may recover actual and consequential damages plus attorney's fees.",
        "compliant_clause_example": "Landlord shall not retaliate against tenant for exercising any rights under Florida Statute Section 83.64 or other applicable law."
    },
    "illegal_provisions_fl": {
        "violation_name": "Prohibited Lease Provisions",
        "requirement": "Certain clauses are void as contrary to public policy",
        "statute": "Florida Statute Section 83.47",
        "statute_text": "Any provision of a rental agreement is void and unenforceable to the extent it waives or precludes the rights, remedies, or requirements set forth in Florida's Residential Landlord and Tenant Act.",
        "severity": "HIGH",
        "category": "Tenant Protections",
        "trigger_keywords": ["waives all rights", "tenant waives", "agrees not to", "forfeits right", "tenant shall not complain"],
        "explanation": "Any lease clause that attempts to waive rights granted by Florida's residential tenancy law is void and unenforceable.",
        "tenant_remedy": "Void clause can be disregarded. Tenant retains all statutory rights under Florida Statute Chapter 83.",
        "compliant_clause_example": "Nothing in this agreement shall be construed to limit tenant's rights under Florida Statute Chapter 83 or other applicable law."
    },
    "self_help_eviction_fl": {
        "violation_name": "Illegal Self-Help Eviction Language",
        "requirement": "Landlord cannot remove tenant except through court process",
        "statute": "Florida Statute Section 83.67",
        "statute_text": "A landlord of any dwelling unit governed by this part shall not cause, directly or indirectly, the interruption or termination of any utility service furnished the tenant, or prevent the tenant from gaining reasonable access to the dwelling unit by any means, other than through judicial process.",
        "severity": "HIGH",
        "category": "Tenant Protections",
        "trigger_keywords": ["lock out", "change locks", "interrupt utilities", "remove tenant", "shut off"],
        "explanation": "Florida strictly prohibits self-help eviction. Landlords cannot lock out tenants or cut utilities; only courts can order removal.",
        "tenant_remedy": "Tenant is entitled to recover actual and consequential damages, plus minimum 3 months rent, and attorney's fees.",
        "compliant_clause_example": "Landlord may not remove tenant or interrupt utility services except through the judicial eviction process as required by Florida Statute Section 83.67."
    }
}


# ============================================================
# ILLINOIS (Chicago RLTO focus)
# ============================================================
ILLINOIS_VIOLATIONS = {
    "deposit_interest_il": {
        "violation_name": "Missing Security Deposit Interest / Improper Handling",
        "requirement": "Chicago landlords must pay interest on deposits held over 6 months",
        "statute": "Chicago Residential Landlord and Tenant Ordinance (RLTO) Section 5-12-082",
        "statute_text": "A landlord who holds a security deposit for a residential unit for more than six months shall pay interest to the tenant accruing from the beginning of the tenancy at the interest rate published annually by the City Comptroller.",
        "severity": "HIGH",
        "category": "Financial",
        "trigger_keywords": ["security deposit", "deposit amount", "interest", "deposit held"],
        "explanation": "Chicago's RLTO requires landlords to pay annual interest on security deposits held more than 6 months and to deposit funds in a federally insured interest-bearing account.",
        "tenant_remedy": "Tenant may recover the deposit plus interest, twice the deposit amount as a penalty, court costs, and attorney's fees.",
        "compliant_clause_example": "Landlord shall hold the security deposit in a federally insured interest-bearing account and pay tenant interest annually per the rate published by the Chicago City Comptroller, as required by RLTO Section 5-12-082."
    },
    "habitability_il": {
        "violation_name": "Waiver of Warranty of Habitability",
        "requirement": "Landlord must maintain premises in habitable condition",
        "statute": "Chicago RLTO Section 5-12-110 / Illinois Common Law",
        "statute_text": "A landlord shall maintain the premises in a habitable condition and in compliance with all applicable provisions of the Chicago Building Code. This warranty of habitability cannot be waived by any lease provision.",
        "severity": "HIGH",
        "category": "Health & Safety",
        "trigger_keywords": ["as-is", "accepts condition", "no warranty", "tenant responsible for all repairs"],
        "explanation": "Illinois common law and the Chicago RLTO establish an implied warranty of habitability that cannot be waived.",
        "tenant_remedy": "Tenant may withhold rent, make repairs and deduct, terminate the lease, or sue for damages.",
        "compliant_clause_example": "Landlord shall maintain the premises in a habitable condition in compliance with the Chicago Building Code, as required by RLTO Section 5-12-110."
    },
    "illegal_entry_il": {
        "violation_name": "Improper Entry Notice Requirements",
        "requirement": "2 days advance notice required for non-emergency entry (Chicago)",
        "statute": "Chicago RLTO Section 5-12-050",
        "statute_text": "A landlord shall not abuse the right of access or use it to harass the tenant. Except in cases of emergency or with tenant consent, the landlord shall provide at least 2 days notice before entry.",
        "severity": "HIGH",
        "category": "Privacy Rights",
        "trigger_keywords": ["enter at any time", "without notice", "24 hour notice", "immediate access", "landlord may enter"],
        "explanation": "Chicago's RLTO requires 2 days notice before entry — stricter than many other jurisdictions. Clauses allowing entry with less notice violate city law.",
        "tenant_remedy": "Refuse unauthorized entry. If landlord repeatedly enters without notice, tenant may terminate the lease and recover damages.",
        "compliant_clause_example": "Landlord shall provide at least 2 days advance notice before entering the premises, except in emergencies, as required by Chicago RLTO Section 5-12-050."
    },
    "retaliation_il": {
        "violation_name": "Retaliatory Conduct by Landlord",
        "protection": "Cannot retaliate against tenants exercising legal rights",
        "statute": "Chicago RLTO Section 5-12-150 / Illinois Statute 765 ILCS 720",
        "statute_text": "It is unlawful for a landlord to retaliate against a tenant by increasing rent, decreasing services, or threatening eviction because the tenant complained to a government agency, exercised a legal right, or organized with other tenants.",
        "severity": "HIGH",
        "category": "Retaliation Protection",
        "trigger_keywords": ["complaints may result", "non-renewal if", "reporting violations", "exercise of rights"],
        "explanation": "Chicago RLTO and Illinois law prohibit landlords from retaliating against tenants who make complaints or exercise their legal rights.",
        "tenant_remedy": "Retaliation is a defense to eviction. Tenant may also recover up to 2 months rent as damages plus attorney's fees.",
        "compliant_clause_example": "Landlord shall not retaliate against tenant for exercising any rights afforded by Chicago RLTO Section 5-12-150 or Illinois law."
    },
    "illegal_fees_il": {
        "violation_name": "Prohibited Fees and Charges",
        "requirement": "Landlords cannot charge fees not permitted by the RLTO",
        "statute": "Chicago RLTO Section 5-12-140",
        "statute_text": "No landlord shall charge a fee for the preparation of a lease or for any service that is not reasonably related to an actual cost incurred by the landlord. Late fees are limited to $10 per month for first $500 of monthly rent, plus 5% for amounts over $500.",
        "severity": "MEDIUM",
        "category": "Financial",
        "trigger_keywords": ["lease preparation fee", "administrative fee", "processing fee", "late fee", "late charge"],
        "explanation": "Chicago's RLTO caps late fees and prohibits many ancillary charges. Lease prep fees and excessive late fees are specifically prohibited.",
        "tenant_remedy": "Refuse to pay prohibited fees. File complaint with City of Chicago's Department of Housing or pursue in court.",
        "compliant_clause_example": "Late fees shall not exceed $10 per month for the first $500 of monthly rent, plus 5% of any amount over $500, per Chicago RLTO Section 5-12-140."
    },
    "deposit_return_il": {
        "violation_name": "Improper Security Deposit Return Timeline",
        "requirement": "Must return deposit within 30 days with itemized statement",
        "statute": "Chicago RLTO Section 5-12-080",
        "statute_text": "Within 30 days after the date that the tenant vacates the dwelling unit, the landlord shall return to the tenant the security deposit or any balance thereof and attach a written statement itemizing the costs of any deductions.",
        "severity": "MEDIUM",
        "category": "Financial",
        "trigger_keywords": ["deposit return", "within 45 days", "within 60 days", "reasonable time", "after surrender"],
        "explanation": "Chicago's RLTO requires return of the deposit (with itemization) within 30 days. Failure to comply triggers significant penalties.",
        "tenant_remedy": "If landlord fails to return deposit within 30 days, tenant may recover twice the deposit plus attorney's fees.",
        "compliant_clause_example": "Security deposit shall be returned with an itemized statement within 30 days of tenant vacating, as required by Chicago RLTO Section 5-12-080."
    },
    "self_help_eviction_il": {
        "violation_name": "Illegal Self-Help Eviction Language",
        "requirement": "Landlord cannot remove tenant except through court process",
        "statute": "Chicago RLTO Section 5-12-160",
        "statute_text": "No landlord shall interfere with the tenant's access to the dwelling unit by changing locks, removing doors, cutting off heat or utilities, or removing tenant's personal property except through the judicial eviction process.",
        "severity": "HIGH",
        "category": "Tenant Protections",
        "trigger_keywords": ["lock out", "change locks", "interrupt utilities", "remove tenant", "shut off"],
        "explanation": "Chicago strictly prohibits self-help eviction. Only courts can order a tenant removed from a dwelling.",
        "tenant_remedy": "Tenant may recover possession, actual damages, 2 months rent as a penalty, and attorney's fees.",
        "compliant_clause_example": "Landlord may not remove tenant or interfere with tenant's access to the premises except through judicial process as required by Chicago RLTO Section 5-12-160."
    }
}


# ============================================================
# STATE REGISTRY
# ============================================================
STATE_KNOWLEDGE_BASES = {
    "California": CALIFORNIA_VIOLATIONS,
    "New York": NEW_YORK_VIOLATIONS,
    "Texas": TEXAS_VIOLATIONS,
    "Florida": FLORIDA_VIOLATIONS,
    "Illinois": ILLINOIS_VIOLATIONS,
}

STATE_CONTEXT = {
    "California": "California (Los Angeles area — subject to LA Rent Stabilization Ordinance and LAMC)",
    "New York": "New York (New York City area — subject to NYC Rent Stabilization and HSTPA 2019)",
    "Texas": "Texas (no statewide rent control — Texas Property Code applies)",
    "Florida": "Florida (Florida Residential Landlord and Tenant Act applies)",
    "Illinois": "Illinois (Chicago area — subject to Chicago Residential Landlord and Tenant Ordinance)",
}

SUPPORTED_STATES = list(STATE_KNOWLEDGE_BASES.keys())

# Cities with notably distinct local tenant ordinances, grouped by state
STATE_CITIES = {
    "California": [
        "Los Angeles",
        "San Francisco",
        "Oakland",
        "Berkeley",
        "Santa Monica",
        "Other (statewide CA law only)",
    ],
    "Illinois": [
        "Chicago",
        "Other (statewide IL law only)",
    ],
}

# Detailed jurisdiction context strings per city — fed directly into the AI prompt
CITY_CONTEXT = {
    # California cities
    "Los Angeles": (
        "California — City of Los Angeles. Statewide California tenant law applies (Civil Code, Health & Safety Code). "
        "Additionally, the LA Rent Stabilization Ordinance (RSO, LAMC §151) covers most units built before Oct 1, 1978: "
        "annual rent increases are capped by LAHD, just-cause eviction is required, and relocation assistance is mandatory "
        "for no-fault evictions. RSO notice (LAMC §151.05) must be provided."
    ),
    "San Francisco": (
        "California — City and County of San Francisco. Statewide California tenant law applies. "
        "Additionally, the San Francisco Rent Ordinance (Admin Code Ch. 37) covers most residential units built before June 13, 1979: "
        "rent increases are limited to the annual CPI allowance set by the SF Rent Board, just-cause eviction is required for all "
        "covered units, and the SF Rent Board provides arbitration. The Residential Rent Stabilization and Arbitration Ordinance "
        "is stricter than statewide law in many respects."
    ),
    "Oakland": (
        "California — City of Oakland. Statewide California tenant law applies. "
        "Additionally, Oakland's Rent Adjustment Program (OMC Ch. 8.22) covers most units built before Jan 1, 1983: "
        "annual rent increases are capped at 60% of CPI (max 10%), just-cause eviction is required (Just Cause for Eviction Ordinance, OMC §8.22.300), "
        "and relocation assistance is required for no-fault evictions. Landlords must register rental units with the city."
    ),
    "Berkeley": (
        "California — City of Berkeley. Statewide California tenant law applies. "
        "Additionally, the Berkeley Rent Stabilization Ordinance (BMC Ch. 13.76) covers most units built before 1980: "
        "rent increases are tied to CPI and require Rent Board approval for above-guideline increases, "
        "just-cause eviction is required, and relocation assistance is required for no-fault evictions. "
        "Berkeley has some of the strongest tenant protections in California."
    ),
    "Santa Monica": (
        "California — City of Santa Monica. Statewide California tenant law applies. "
        "Additionally, the Santa Monica Rent Control Charter Amendment covers most units built before April 10, 1979: "
        "rents are controlled by the Santa Monica Rent Control Board, annual increases are strictly limited, "
        "just-cause eviction is required, and relocation fees are required for no-fault evictions. "
        "Santa Monica's rent control is among the strictest in the state."
    ),
    "Other (statewide CA law only)": (
        "California — jurisdiction outside major rent-control cities. Only statewide California tenant law applies: "
        "Civil Code (security deposits, habitability, entry notice, repair rights, retaliation), "
        "Health & Safety Code (mold, bedbug disclosures), and AB 1482 (statewide rent cap of 5%+CPI for qualifying units). "
        "No local rent stabilization ordinance applies."
    ),
    # Illinois cities
    "Chicago": (
        "Illinois — City of Chicago. The Chicago Residential Landlord and Tenant Ordinance (RLTO, Ch. 5-12) applies to "
        "most residential rental units in Chicago: security deposit interest is required, entry requires 2 days notice, "
        "late fees are capped, and self-help eviction is prohibited. Illinois statewide landlord-tenant law also applies."
    ),
    "Other (statewide IL law only)": (
        "Illinois — jurisdiction outside Chicago. Only statewide Illinois landlord-tenant law applies. "
        "The Chicago RLTO does not apply. Key protections include implied warranty of habitability and anti-retaliation provisions "
        "under Illinois statute 765 ILCS 710-740."
    ),
}

# Backward-compatible alias
LA_LEASE_VIOLATIONS = CALIFORNIA_VIOLATIONS


# ============================================================
# HELPER FUNCTIONS
# ============================================================
def get_violations_for_state(state):
    return STATE_KNOWLEDGE_BASES.get(state, CALIFORNIA_VIOLATIONS)

def get_jurisdiction_context(state, city=None):
    """Return the detailed jurisdiction context string for the AI prompt."""
    if city and city in CITY_CONTEXT:
        return CITY_CONTEXT[city]
    return STATE_CONTEXT.get(state, state)

def get_cities_for_state(state):
    """Return list of notable cities for a state, or empty list if none defined."""
    return STATE_CITIES.get(state, [])

def get_all_violations():
    return list(CALIFORNIA_VIOLATIONS.keys())

def get_violations_by_severity(severity):
    return {k: v for k, v in CALIFORNIA_VIOLATIONS.items() if v["severity"] == severity}

def get_violations_by_category(category):
    return {k: v for k, v in CALIFORNIA_VIOLATIONS.items() if v["category"] == category}


if __name__ == "__main__":
    for state, kb in STATE_KNOWLEDGE_BASES.items():
        print(f"{state}: {len(kb)} violations")
