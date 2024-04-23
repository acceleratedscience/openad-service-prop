tests = []

tests.append(
    {
        "service_type": "get_molecule_property",
        "service_name": "get molecule tox21",
        "parameters": {
            "property_type": [
                "tox21",
            ],
            "site": "Kidney",
            "algorithm_version": "v0",
            "subjects": [
                "CCO",
            ],
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)
tests.append(
    {
        "service_type": "get_molecule_property",
        "service_name": "get molecule sider",
        "parameters": {
            "property_type": [
                "sider",
            ],
            "site": "Kidney",
            "algorithm_version": "v0",
            "subjects": [
                "CCO",
            ],
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)
tests.append(
    {
        "service_type": "get_molecule_property",
        "service_name": "get molecule organtox",
        "parameters": {
            "property_type": [
                "organtox",
            ],
            "site": "Kidney",
            "algorithm_version": "v0",
            "subjects": [
                "CCO",
            ],
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)
tests.append(
    {
        "service_type": "get_molecule_property",
        "service_name": "get molecule clintox",
        "parameters": {
            "property_type": [
                "clintox",
            ],
            "algorithm_version": "v0",
            "subjects": [
                "CCO",
            ],
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)
tests.append(
    {
        "service_type": "get_molecule_property",
        "service_name": "get molecule properties 1",
        "parameters": {
            "property_type": [
                "molecular_weight",
                "number_of_aromatic_rings",
                "number_of_h_acceptors",
                "number_of_h_donors",
                "number_of_atoms",
                "number_of_rings",
                "number_of_rotatable_bonds",
                "number_of_large_rings",
                "number_of_heterocycles",
                "number_of_stereocenters",
                "is_scaffold",
                "bertz",
                "tpsa",
                "logp",
                "qed",
                "plogp",
                "penalized_logp",
                "lipinski",
                "sas",
                "esol",
            ],
            "subjects": ["C12C=CC=NN1C(C#CC1=C(C)C=CC3C(NC4=CC(C(F)(F)F)=CC=C4)=NOC1=3)=CN=2"],
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)

tests.append(
    {
        "service_name": "get molecule scscore",
        "service_type": "get_molecule_property",
        "parameters": {
            "property_type": [
                "scscore",
            ],
            "subjects": [
                "CCO",
                "C1C2C(COC2O)C(O1)C3=CC4=C(C=C3)OCO4",
                "C1=C(N=NN1CC(C(=O)O)N)P(=O)(O)O",
                "C1=CC=C(C=C1)C2(C(=O)[N-]C(=O)N2)C3=CC=CC=C3.[Na+]",
                "CC1(CC(C2(C1C(OC=C2)OC3C(C(C(C(O3)CO)O)O)O)O)O)O ",
                "CC(C)(C)OC(=O)NC(CC1=CC=CC=C1)C(C[N+](C)(CC2=CC=CC=C2)NC(=O)C3=CC=CC=C3)O",
                "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O",
            ],
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)

tests.append(
    {
        "service_name": "get molecule activity_against_target",
        "service_type": "get_molecule_property",
        "parameters": {
            "property_type": [
                "activity_against_target",
            ],
            "subjects": [
                "CCO",
                "C1C2C(COC2O)C(O1)C3=CC4=C(C=C3)OCO4",
                "C1=C(N=NN1CC(C(=O)O)N)P(=O)(O)O",
                "C1=CC=C(C=C1)C2(C(=O)[N-]C(=O)N2)C3=CC=CC=C3.[Na+]",
                "CC1(CC(C2(C1C(OC=C2)OC3C(C(C(C(O3)CO)O)O)O)O)O)O ",
                "CC(C)(C)OC(=O)NC(CC1=CC=CC=C1)C(C[N+](C)(CC2=CC=CC=C2)NC(=O)C3=CC=CC=C3)O",
                "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O",
            ],
            "target": "drd2",
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)


tests.append(
    {
        "service_name": "get molecule similarity_seed",
        "service_type": "get_molecule_property",
        "parameters": {
            "property_type": [
                "similarity_seed",
            ],
            "subjects": [
                "CCO",
                "C1C2C(COC2O)C(O1)C3=CC4=C(C=C3)OCO4",
                "C1=C(N=NN1CC(C(=O)O)N)P(=O)(O)O",
                "C1=CC=C(C=C1)C2(C(=O)[N-]C(=O)N2)C3=CC=CC=C3.[Na+]",
                "CC1(CC(C2(C1C(OC=C2)OC3C(C(C(C(O3)CO)O)O)O)O)O)O ",
                "CC(C)(C)OC(=O)NC(CC1=CC=CC=C1)C(C[N+](C)(CC2=CC=CC=C2)NC(=O)C3=CC=CC=C3)O",
                "CC(C)CC1=CC=C(C=C1)C(C)C(=O)O",
            ],
            "smiles": "CCO",
            "subject_type": "smiles",
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)


tests.append(
    {
        "service_name": "get protein properties 1",
        "service_type": "get_protein_property",
        "parameters": {
            "property_type": ["length", "boman_index", "aliphaticity", "hydrophobicity", "aromaticity", "instability"],
            "subjects": ["KFLIYQMECSTMIFGL"],
            "subject_type": "protein",
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)

tests.append(
    {
        "service_name": "get protein properties 3",
        "service_type": "get_protein_property",
        "parameters": {
            "property_type": ["charge_density"],
            "subjects": ["KFLIYQMECSTMIFGL"],
            "subject_type": "protein",
            "Ph": 7.1,
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)
tests.append(
    {
        "service_name": "get protein properties 3",
        "service_type": "get_protein_property",
        "parameters": {
            "property_type": ["charge"],
            "subjects": ["KFLIYQMECSTMIFGL"],
            "subject_type": "protein",
            "Ph": 7.1,
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)

tests.append(
    {
        "service_name": "get protein properties 2",
        "service_type": "get_protein_property",
        "parameters": {
            "property_type": ["protein_weight"],
            "subjects": ["KFLIYQMECSTMIFGL"],
            "subject_type": "protein",
            "amide": False,
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)
tests.append(
    {
        "service_name": "get protein properties 2",
        "service_type": "get_protein_property",
        "parameters": {
            "property_type": ["isoelectric_point"],
            "subjects": ["KFLIYQMECSTMIFGL"],
            "subject_type": "protein",
            "amide": True,
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)


tests.append(
    {
        "service_type": "get_crystal_property",
        "service_name": "get crystal formation_energy",
        "parameters": {
            "property_type": [
                "formation_energy",
            ],
            "algorithm_version": "v0",
            "subjects": [
                [
                    "1000041.cif",
                    "#------------------------------------------------------------------------------\n#$Date: 2015-01-27 21:58:39 +0200 (Tue, 27 Jan 2015) $\n#$Revision: 130149 $\n#$URL: svn://www.crystallography.net/cod/cif/1/00/00/1000041.cif $\n#------------------------------------------------------------------------------\n#\n# This file is available in the Crystallography Open Database (COD),\n# http://www.crystallography.net/\n#\n# All data on this site have been placed in the public domain by the\n# contributors.\n#\ndata_1000041\nloop_\n_publ_author_name\n'Abrahams, S C'\n'Bernstein, J L'\n_publ_section_title\n;\nAccuracy of an automatic diffractometer. measurement of the sodium\nchloride structure factors\n;\n_journal_coden_ASTM              ACCRA9\n_journal_name_full               'Acta Crystallographica (1,1948-23,1967)'\n_journal_page_first              926\n_journal_page_last               932\n_journal_paper_doi               10.1107/S0365110X65002244\n_journal_volume                  18\n_journal_year                    1965\n_chemical_formula_structural     'Na Cl'\n_chemical_formula_sum            'Cl Na'\n_chemical_name_systematic        'Sodium chloride'\n_space_group_IT_number           225\n_symmetry_cell_setting           cubic\n_symmetry_Int_Tables_number      225\n_symmetry_space_group_name_Hall  '-F 4 2 3'\n_symmetry_space_group_name_H-M   'F m -3 m'\n_cell_angle_alpha                90\n_cell_angle_beta                 90\n_cell_angle_gamma                90\n_cell_formula_units_Z            4\n_cell_length_a                   5.62\n_cell_length_b                   5.62\n_cell_length_c                   5.62\n_cell_volume                     177.5\n_refine_ls_R_factor_all          0.022\n_cod_database_code               1000041\nloop_\n_symmetry_equiv_pos_as_xyz\nx,y,z\ny,z,x\nz,x,y\nx,z,y\ny,x,z\nz,y,x\nx,-y,-z\ny,-z,-x\nz,-x,-y\nx,-z,-y\ny,-x,-z\nz,-y,-x\n-x,y,-z\n-y,z,-x\n-z,x,-y\n-x,z,-y\n-y,x,-z\n-z,y,-x\n-x,-y,z\n-y,-z,x\n-z,-x,y\n-x,-z,y\n-y,-x,z\n-z,-y,x\n-x,-y,-z\n-y,-z,-x\n-z,-x,-y\n-x,-z,-y\n-y,-x,-z\n-z,-y,-x\n-x,y,z\n-y,z,x\n-z,x,y\n-x,z,y\n-y,x,z\n-z,y,x\nx,-y,z\ny,-z,x\nz,-x,y\nx,-z,y\ny,-x,z\nz,-y,x\nx,y,-z\ny,z,-x\nz,x,-y\nx,z,-y\ny,x,-z\nz,y,-x\nx,1/2+y,1/2+z\n1/2+x,y,1/2+z\n1/2+x,1/2+y,z\ny,1/2+z,1/2+x\n1/2+y,z,1/2+x\n1/2+y,1/2+z,x\nz,1/2+x,1/2+y\n1/2+z,x,1/2+y\n1/2+z,1/2+x,y\nx,1/2+z,1/2+y\n1/2+x,z,1/2+y\n1/2+x,1/2+z,y\ny,1/2+x,1/2+z\n1/2+y,x,1/2+z\n1/2+y,1/2+x,z\nz,1/2+y,1/2+x\n1/2+z,y,1/2+x\n1/2+z,1/2+y,x\nx,1/2-y,1/2-z\n1/2+x,-y,1/2-z\n1/2+x,1/2-y,-z\ny,1/2-z,1/2-x\n1/2+y,-z,1/2-x\n1/2+y,1/2-z,-x\nz,1/2-x,1/2-y\n1/2+z,-x,1/2-y\n1/2+z,1/2-x,-y\nx,1/2-z,1/2-y\n1/2+x,-z,1/2-y\n1/2+x,1/2-z,-y\ny,1/2-x,1/2-z\n1/2+y,-x,1/2-z\n1/2+y,1/2-x,-z\nz,1/2-y,1/2-x\n1/2+z,-y,1/2-x\n1/2+z,1/2-y,-x\n-x,1/2+y,1/2-z\n1/2-x,y,1/2-z\n1/2-x,1/2+y,-z\n-y,1/2+z,1/2-x\n1/2-y,z,1/2-x\n1/2-y,1/2+z,-x\n-z,1/2+x,1/2-y\n1/2-z,x,1/2-y\n1/2-z,1/2+x,-y\n-x,1/2+z,1/2-y\n1/2-x,z,1/2-y\n1/2-x,1/2+z,-y\n-y,1/2+x,1/2-z\n1/2-y,x,1/2-z\n1/2-y,1/2+x,-z\n-z,1/2+y,1/2-x\n1/2-z,y,1/2-x\n1/2-z,1/2+y,-x\n-x,1/2-y,1/2+z\n1/2-x,-y,1/2+z\n1/2-x,1/2-y,z\n-y,1/2-z,1/2+x\n1/2-y,-z,1/2+x\n1/2-y,1/2-z,x\n-z,1/2-x,1/2+y\n1/2-z,-x,1/2+y\n1/2-z,1/2-x,y\n-x,1/2-z,1/2+y\n1/2-x,-z,1/2+y\n1/2-x,1/2-z,y\n-y,1/2-x,1/2+z\n1/2-y,-x,1/2+z\n1/2-y,1/2-x,z\n-z,1/2-y,1/2+x\n1/2-z,-y,1/2+x\n1/2-z,1/2-y,x\n-x,1/2-y,1/2-z\n1/2-x,-y,1/2-z\n1/2-x,1/2-y,-z\n-y,1/2-z,1/2-x\n1/2-y,-z,1/2-x\n1/2-y,1/2-z,-x\n-z,1/2-x,1/2-y\n1/2-z,-x,1/2-y\n1/2-z,1/2-x,-y\n-x,1/2-z,1/2-y\n1/2-x,-z,1/2-y\n1/2-x,1/2-z,-y\n-y,1/2-x,1/2-z\n1/2-y,-x,1/2-z\n1/2-y,1/2-x,-z\n-z,1/2-y,1/2-x\n1/2-z,-y,1/2-x\n1/2-z,1/2-y,-x\n-x,1/2+y,1/2+z\n1/2-x,y,1/2+z\n1/2-x,1/2+y,z\n-y,1/2+z,1/2+x\n1/2-y,z,1/2+x\n1/2-y,1/2+z,x\n-z,1/2+x,1/2+y\n1/2-z,x,1/2+y\n1/2-z,1/2+x,y\n-x,1/2+z,1/2+y\n1/2-x,z,1/2+y\n1/2-x,1/2+z,y\n-y,1/2+x,1/2+z\n1/2-y,x,1/2+z\n1/2-y,1/2+x,z\n-z,1/2+y,1/2+x\n1/2-z,y,1/2+x\n1/2-z,1/2+y,x\nx,1/2-y,1/2+z\n1/2+x,-y,1/2+z\n1/2+x,1/2-y,z\ny,1/2-z,1/2+x\n1/2+y,-z,1/2+x\n1/2+y,1/2-z,x\nz,1/2-x,1/2+y\n1/2+z,-x,1/2+y\n1/2+z,1/2-x,y\nx,1/2-z,1/2+y\n1/2+x,-z,1/2+y\n1/2+x,1/2-z,y\ny,1/2-x,1/2+z\n1/2+y,-x,1/2+z\n1/2+y,1/2-x,z\nz,1/2-y,1/2+x\n1/2+z,-y,1/2+x\n1/2+z,1/2-y,x\nx,1/2+y,1/2-z\n1/2+x,y,1/2-z\n1/2+x,1/2+y,-z\ny,1/2+z,1/2-x\n1/2+y,z,1/2-x\n1/2+y,1/2+z,-x\nz,1/2+x,1/2-y\n1/2+z,x,1/2-y\n1/2+z,1/2+x,-y\nx,1/2+z,1/2-y\n1/2+x,z,1/2-y\n1/2+x,1/2+z,-y\ny,1/2+x,1/2-z\n1/2+y,x,1/2-z\n1/2+y,1/2+x,-z\nz,1/2+y,1/2-x\n1/2+z,y,1/2-x\n1/2+z,1/2+y,-x\nloop_\n_atom_site_label\n_atom_site_type_symbol\n_atom_site_symmetry_multiplicity\n_atom_site_Wyckoff_symbol\n_atom_site_fract_x\n_atom_site_fract_y\n_atom_site_fract_z\n_atom_site_occupancy\n_atom_site_attached_hydrogens\n_atom_site_calc_flag\nNa1 Na1+ 4 a 0. 0. 0. 1. 0 d\nCl1 Cl1- 4 b 0.5 0.5 0.5 1. 0 d\nloop_\n_atom_type_symbol\n_atom_type_oxidation_number\nNa1+ 1.000\nCl1- -1.000\n",
                ]
            ],
            "subject_type": "CIF",
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)


tests.append(
    {
        "service_type": "get_crystal_property",
        "service_name": "get crystal absolute_energy",
        "parameters": {
            "property_type": [
                "absolute_energy",
            ],
            "algorithm_version": "v0",
            "subjects": [
                [
                    "1000041.cif",
                    "#------------------------------------------------------------------------------\n#$Date: 2015-01-27 21:58:39 +0200 (Tue, 27 Jan 2015) $\n#$Revision: 130149 $\n#$URL: svn://www.crystallography.net/cod/cif/1/00/00/1000041.cif $\n#------------------------------------------------------------------------------\n#\n# This file is available in the Crystallography Open Database (COD),\n# http://www.crystallography.net/\n#\n# All data on this site have been placed in the public domain by the\n# contributors.\n#\ndata_1000041\nloop_\n_publ_author_name\n'Abrahams, S C'\n'Bernstein, J L'\n_publ_section_title\n;\nAccuracy of an automatic diffractometer. measurement of the sodium\nchloride structure factors\n;\n_journal_coden_ASTM              ACCRA9\n_journal_name_full               'Acta Crystallographica (1,1948-23,1967)'\n_journal_page_first              926\n_journal_page_last               932\n_journal_paper_doi               10.1107/S0365110X65002244\n_journal_volume                  18\n_journal_year                    1965\n_chemical_formula_structural     'Na Cl'\n_chemical_formula_sum            'Cl Na'\n_chemical_name_systematic        'Sodium chloride'\n_space_group_IT_number           225\n_symmetry_cell_setting           cubic\n_symmetry_Int_Tables_number      225\n_symmetry_space_group_name_Hall  '-F 4 2 3'\n_symmetry_space_group_name_H-M   'F m -3 m'\n_cell_angle_alpha                90\n_cell_angle_beta                 90\n_cell_angle_gamma                90\n_cell_formula_units_Z            4\n_cell_length_a                   5.62\n_cell_length_b                   5.62\n_cell_length_c                   5.62\n_cell_volume                     177.5\n_refine_ls_R_factor_all          0.022\n_cod_database_code               1000041\nloop_\n_symmetry_equiv_pos_as_xyz\nx,y,z\ny,z,x\nz,x,y\nx,z,y\ny,x,z\nz,y,x\nx,-y,-z\ny,-z,-x\nz,-x,-y\nx,-z,-y\ny,-x,-z\nz,-y,-x\n-x,y,-z\n-y,z,-x\n-z,x,-y\n-x,z,-y\n-y,x,-z\n-z,y,-x\n-x,-y,z\n-y,-z,x\n-z,-x,y\n-x,-z,y\n-y,-x,z\n-z,-y,x\n-x,-y,-z\n-y,-z,-x\n-z,-x,-y\n-x,-z,-y\n-y,-x,-z\n-z,-y,-x\n-x,y,z\n-y,z,x\n-z,x,y\n-x,z,y\n-y,x,z\n-z,y,x\nx,-y,z\ny,-z,x\nz,-x,y\nx,-z,y\ny,-x,z\nz,-y,x\nx,y,-z\ny,z,-x\nz,x,-y\nx,z,-y\ny,x,-z\nz,y,-x\nx,1/2+y,1/2+z\n1/2+x,y,1/2+z\n1/2+x,1/2+y,z\ny,1/2+z,1/2+x\n1/2+y,z,1/2+x\n1/2+y,1/2+z,x\nz,1/2+x,1/2+y\n1/2+z,x,1/2+y\n1/2+z,1/2+x,y\nx,1/2+z,1/2+y\n1/2+x,z,1/2+y\n1/2+x,1/2+z,y\ny,1/2+x,1/2+z\n1/2+y,x,1/2+z\n1/2+y,1/2+x,z\nz,1/2+y,1/2+x\n1/2+z,y,1/2+x\n1/2+z,1/2+y,x\nx,1/2-y,1/2-z\n1/2+x,-y,1/2-z\n1/2+x,1/2-y,-z\ny,1/2-z,1/2-x\n1/2+y,-z,1/2-x\n1/2+y,1/2-z,-x\nz,1/2-x,1/2-y\n1/2+z,-x,1/2-y\n1/2+z,1/2-x,-y\nx,1/2-z,1/2-y\n1/2+x,-z,1/2-y\n1/2+x,1/2-z,-y\ny,1/2-x,1/2-z\n1/2+y,-x,1/2-z\n1/2+y,1/2-x,-z\nz,1/2-y,1/2-x\n1/2+z,-y,1/2-x\n1/2+z,1/2-y,-x\n-x,1/2+y,1/2-z\n1/2-x,y,1/2-z\n1/2-x,1/2+y,-z\n-y,1/2+z,1/2-x\n1/2-y,z,1/2-x\n1/2-y,1/2+z,-x\n-z,1/2+x,1/2-y\n1/2-z,x,1/2-y\n1/2-z,1/2+x,-y\n-x,1/2+z,1/2-y\n1/2-x,z,1/2-y\n1/2-x,1/2+z,-y\n-y,1/2+x,1/2-z\n1/2-y,x,1/2-z\n1/2-y,1/2+x,-z\n-z,1/2+y,1/2-x\n1/2-z,y,1/2-x\n1/2-z,1/2+y,-x\n-x,1/2-y,1/2+z\n1/2-x,-y,1/2+z\n1/2-x,1/2-y,z\n-y,1/2-z,1/2+x\n1/2-y,-z,1/2+x\n1/2-y,1/2-z,x\n-z,1/2-x,1/2+y\n1/2-z,-x,1/2+y\n1/2-z,1/2-x,y\n-x,1/2-z,1/2+y\n1/2-x,-z,1/2+y\n1/2-x,1/2-z,y\n-y,1/2-x,1/2+z\n1/2-y,-x,1/2+z\n1/2-y,1/2-x,z\n-z,1/2-y,1/2+x\n1/2-z,-y,1/2+x\n1/2-z,1/2-y,x\n-x,1/2-y,1/2-z\n1/2-x,-y,1/2-z\n1/2-x,1/2-y,-z\n-y,1/2-z,1/2-x\n1/2-y,-z,1/2-x\n1/2-y,1/2-z,-x\n-z,1/2-x,1/2-y\n1/2-z,-x,1/2-y\n1/2-z,1/2-x,-y\n-x,1/2-z,1/2-y\n1/2-x,-z,1/2-y\n1/2-x,1/2-z,-y\n-y,1/2-x,1/2-z\n1/2-y,-x,1/2-z\n1/2-y,1/2-x,-z\n-z,1/2-y,1/2-x\n1/2-z,-y,1/2-x\n1/2-z,1/2-y,-x\n-x,1/2+y,1/2+z\n1/2-x,y,1/2+z\n1/2-x,1/2+y,z\n-y,1/2+z,1/2+x\n1/2-y,z,1/2+x\n1/2-y,1/2+z,x\n-z,1/2+x,1/2+y\n1/2-z,x,1/2+y\n1/2-z,1/2+x,y\n-x,1/2+z,1/2+y\n1/2-x,z,1/2+y\n1/2-x,1/2+z,y\n-y,1/2+x,1/2+z\n1/2-y,x,1/2+z\n1/2-y,1/2+x,z\n-z,1/2+y,1/2+x\n1/2-z,y,1/2+x\n1/2-z,1/2+y,x\nx,1/2-y,1/2+z\n1/2+x,-y,1/2+z\n1/2+x,1/2-y,z\ny,1/2-z,1/2+x\n1/2+y,-z,1/2+x\n1/2+y,1/2-z,x\nz,1/2-x,1/2+y\n1/2+z,-x,1/2+y\n1/2+z,1/2-x,y\nx,1/2-z,1/2+y\n1/2+x,-z,1/2+y\n1/2+x,1/2-z,y\ny,1/2-x,1/2+z\n1/2+y,-x,1/2+z\n1/2+y,1/2-x,z\nz,1/2-y,1/2+x\n1/2+z,-y,1/2+x\n1/2+z,1/2-y,x\nx,1/2+y,1/2-z\n1/2+x,y,1/2-z\n1/2+x,1/2+y,-z\ny,1/2+z,1/2-x\n1/2+y,z,1/2-x\n1/2+y,1/2+z,-x\nz,1/2+x,1/2-y\n1/2+z,x,1/2-y\n1/2+z,1/2+x,-y\nx,1/2+z,1/2-y\n1/2+x,z,1/2-y\n1/2+x,1/2+z,-y\ny,1/2+x,1/2-z\n1/2+y,x,1/2-z\n1/2+y,1/2+x,-z\nz,1/2+y,1/2-x\n1/2+z,y,1/2-x\n1/2+z,1/2+y,-x\nloop_\n_atom_site_label\n_atom_site_type_symbol\n_atom_site_symmetry_multiplicity\n_atom_site_Wyckoff_symbol\n_atom_site_fract_x\n_atom_site_fract_y\n_atom_site_fract_z\n_atom_site_occupancy\n_atom_site_attached_hydrogens\n_atom_site_calc_flag\nNa1 Na1+ 4 a 0. 0. 0. 1. 0 d\nCl1 Cl1- 4 b 0.5 0.5 0.5 1. 0 d\nloop_\n_atom_type_symbol\n_atom_type_oxidation_number\nNa1+ 1.000\nCl1- -1.000\n",
                ]
            ],
            "subject_type": "CIF",
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)
tests.append(
    {
        "service_type": "get_crystal_property",
        "service_name": "get crystal band_gap",
        "parameters": {
            "property_type": [
                "band_gap",
            ],
            "algorithm_version": "v0",
            "subjects": [
                [
                    "1000041.cif",
                    "#------------------------------------------------------------------------------\n#$Date: 2015-01-27 21:58:39 +0200 (Tue, 27 Jan 2015) $\n#$Revision: 130149 $\n#$URL: svn://www.crystallography.net/cod/cif/1/00/00/1000041.cif $\n#------------------------------------------------------------------------------\n#\n# This file is available in the Crystallography Open Database (COD),\n# http://www.crystallography.net/\n#\n# All data on this site have been placed in the public domain by the\n# contributors.\n#\ndata_1000041\nloop_\n_publ_author_name\n'Abrahams, S C'\n'Bernstein, J L'\n_publ_section_title\n;\nAccuracy of an automatic diffractometer. measurement of the sodium\nchloride structure factors\n;\n_journal_coden_ASTM              ACCRA9\n_journal_name_full               'Acta Crystallographica (1,1948-23,1967)'\n_journal_page_first              926\n_journal_page_last               932\n_journal_paper_doi               10.1107/S0365110X65002244\n_journal_volume                  18\n_journal_year                    1965\n_chemical_formula_structural     'Na Cl'\n_chemical_formula_sum            'Cl Na'\n_chemical_name_systematic        'Sodium chloride'\n_space_group_IT_number           225\n_symmetry_cell_setting           cubic\n_symmetry_Int_Tables_number      225\n_symmetry_space_group_name_Hall  '-F 4 2 3'\n_symmetry_space_group_name_H-M   'F m -3 m'\n_cell_angle_alpha                90\n_cell_angle_beta                 90\n_cell_angle_gamma                90\n_cell_formula_units_Z            4\n_cell_length_a                   5.62\n_cell_length_b                   5.62\n_cell_length_c                   5.62\n_cell_volume                     177.5\n_refine_ls_R_factor_all          0.022\n_cod_database_code               1000041\nloop_\n_symmetry_equiv_pos_as_xyz\nx,y,z\ny,z,x\nz,x,y\nx,z,y\ny,x,z\nz,y,x\nx,-y,-z\ny,-z,-x\nz,-x,-y\nx,-z,-y\ny,-x,-z\nz,-y,-x\n-x,y,-z\n-y,z,-x\n-z,x,-y\n-x,z,-y\n-y,x,-z\n-z,y,-x\n-x,-y,z\n-y,-z,x\n-z,-x,y\n-x,-z,y\n-y,-x,z\n-z,-y,x\n-x,-y,-z\n-y,-z,-x\n-z,-x,-y\n-x,-z,-y\n-y,-x,-z\n-z,-y,-x\n-x,y,z\n-y,z,x\n-z,x,y\n-x,z,y\n-y,x,z\n-z,y,x\nx,-y,z\ny,-z,x\nz,-x,y\nx,-z,y\ny,-x,z\nz,-y,x\nx,y,-z\ny,z,-x\nz,x,-y\nx,z,-y\ny,x,-z\nz,y,-x\nx,1/2+y,1/2+z\n1/2+x,y,1/2+z\n1/2+x,1/2+y,z\ny,1/2+z,1/2+x\n1/2+y,z,1/2+x\n1/2+y,1/2+z,x\nz,1/2+x,1/2+y\n1/2+z,x,1/2+y\n1/2+z,1/2+x,y\nx,1/2+z,1/2+y\n1/2+x,z,1/2+y\n1/2+x,1/2+z,y\ny,1/2+x,1/2+z\n1/2+y,x,1/2+z\n1/2+y,1/2+x,z\nz,1/2+y,1/2+x\n1/2+z,y,1/2+x\n1/2+z,1/2+y,x\nx,1/2-y,1/2-z\n1/2+x,-y,1/2-z\n1/2+x,1/2-y,-z\ny,1/2-z,1/2-x\n1/2+y,-z,1/2-x\n1/2+y,1/2-z,-x\nz,1/2-x,1/2-y\n1/2+z,-x,1/2-y\n1/2+z,1/2-x,-y\nx,1/2-z,1/2-y\n1/2+x,-z,1/2-y\n1/2+x,1/2-z,-y\ny,1/2-x,1/2-z\n1/2+y,-x,1/2-z\n1/2+y,1/2-x,-z\nz,1/2-y,1/2-x\n1/2+z,-y,1/2-x\n1/2+z,1/2-y,-x\n-x,1/2+y,1/2-z\n1/2-x,y,1/2-z\n1/2-x,1/2+y,-z\n-y,1/2+z,1/2-x\n1/2-y,z,1/2-x\n1/2-y,1/2+z,-x\n-z,1/2+x,1/2-y\n1/2-z,x,1/2-y\n1/2-z,1/2+x,-y\n-x,1/2+z,1/2-y\n1/2-x,z,1/2-y\n1/2-x,1/2+z,-y\n-y,1/2+x,1/2-z\n1/2-y,x,1/2-z\n1/2-y,1/2+x,-z\n-z,1/2+y,1/2-x\n1/2-z,y,1/2-x\n1/2-z,1/2+y,-x\n-x,1/2-y,1/2+z\n1/2-x,-y,1/2+z\n1/2-x,1/2-y,z\n-y,1/2-z,1/2+x\n1/2-y,-z,1/2+x\n1/2-y,1/2-z,x\n-z,1/2-x,1/2+y\n1/2-z,-x,1/2+y\n1/2-z,1/2-x,y\n-x,1/2-z,1/2+y\n1/2-x,-z,1/2+y\n1/2-x,1/2-z,y\n-y,1/2-x,1/2+z\n1/2-y,-x,1/2+z\n1/2-y,1/2-x,z\n-z,1/2-y,1/2+x\n1/2-z,-y,1/2+x\n1/2-z,1/2-y,x\n-x,1/2-y,1/2-z\n1/2-x,-y,1/2-z\n1/2-x,1/2-y,-z\n-y,1/2-z,1/2-x\n1/2-y,-z,1/2-x\n1/2-y,1/2-z,-x\n-z,1/2-x,1/2-y\n1/2-z,-x,1/2-y\n1/2-z,1/2-x,-y\n-x,1/2-z,1/2-y\n1/2-x,-z,1/2-y\n1/2-x,1/2-z,-y\n-y,1/2-x,1/2-z\n1/2-y,-x,1/2-z\n1/2-y,1/2-x,-z\n-z,1/2-y,1/2-x\n1/2-z,-y,1/2-x\n1/2-z,1/2-y,-x\n-x,1/2+y,1/2+z\n1/2-x,y,1/2+z\n1/2-x,1/2+y,z\n-y,1/2+z,1/2+x\n1/2-y,z,1/2+x\n1/2-y,1/2+z,x\n-z,1/2+x,1/2+y\n1/2-z,x,1/2+y\n1/2-z,1/2+x,y\n-x,1/2+z,1/2+y\n1/2-x,z,1/2+y\n1/2-x,1/2+z,y\n-y,1/2+x,1/2+z\n1/2-y,x,1/2+z\n1/2-y,1/2+x,z\n-z,1/2+y,1/2+x\n1/2-z,y,1/2+x\n1/2-z,1/2+y,x\nx,1/2-y,1/2+z\n1/2+x,-y,1/2+z\n1/2+x,1/2-y,z\ny,1/2-z,1/2+x\n1/2+y,-z,1/2+x\n1/2+y,1/2-z,x\nz,1/2-x,1/2+y\n1/2+z,-x,1/2+y\n1/2+z,1/2-x,y\nx,1/2-z,1/2+y\n1/2+x,-z,1/2+y\n1/2+x,1/2-z,y\ny,1/2-x,1/2+z\n1/2+y,-x,1/2+z\n1/2+y,1/2-x,z\nz,1/2-y,1/2+x\n1/2+z,-y,1/2+x\n1/2+z,1/2-y,x\nx,1/2+y,1/2-z\n1/2+x,y,1/2-z\n1/2+x,1/2+y,-z\ny,1/2+z,1/2-x\n1/2+y,z,1/2-x\n1/2+y,1/2+z,-x\nz,1/2+x,1/2-y\n1/2+z,x,1/2-y\n1/2+z,1/2+x,-y\nx,1/2+z,1/2-y\n1/2+x,z,1/2-y\n1/2+x,1/2+z,-y\ny,1/2+x,1/2-z\n1/2+y,x,1/2-z\n1/2+y,1/2+x,-z\nz,1/2+y,1/2-x\n1/2+z,y,1/2-x\n1/2+z,1/2+y,-x\nloop_\n_atom_site_label\n_atom_site_type_symbol\n_atom_site_symmetry_multiplicity\n_atom_site_Wyckoff_symbol\n_atom_site_fract_x\n_atom_site_fract_y\n_atom_site_fract_z\n_atom_site_occupancy\n_atom_site_attached_hydrogens\n_atom_site_calc_flag\nNa1 Na1+ 4 a 0. 0. 0. 1. 0 d\nCl1 Cl1- 4 b 0.5 0.5 0.5 1. 0 d\nloop_\n_atom_type_symbol\n_atom_type_oxidation_number\nNa1+ 1.000\nCl1- -1.000\n",
                ]
            ],
            "subject_type": "CIF",
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)
tests.append(
    {
        "service_type": "get_crystal_property",
        "service_name": "get crystal fermi_energy",
        "parameters": {
            "property_type": [
                "fermi_energy",
            ],
            "algorithm_version": "v0",
            "subjects": [
                [
                    "1000041.cif",
                    "#------------------------------------------------------------------------------\n#$Date: 2015-01-27 21:58:39 +0200 (Tue, 27 Jan 2015) $\n#$Revision: 130149 $\n#$URL: svn://www.crystallography.net/cod/cif/1/00/00/1000041.cif $\n#------------------------------------------------------------------------------\n#\n# This file is available in the Crystallography Open Database (COD),\n# http://www.crystallography.net/\n#\n# All data on this site have been placed in the public domain by the\n# contributors.\n#\ndata_1000041\nloop_\n_publ_author_name\n'Abrahams, S C'\n'Bernstein, J L'\n_publ_section_title\n;\nAccuracy of an automatic diffractometer. measurement of the sodium\nchloride structure factors\n;\n_journal_coden_ASTM              ACCRA9\n_journal_name_full               'Acta Crystallographica (1,1948-23,1967)'\n_journal_page_first              926\n_journal_page_last               932\n_journal_paper_doi               10.1107/S0365110X65002244\n_journal_volume                  18\n_journal_year                    1965\n_chemical_formula_structural     'Na Cl'\n_chemical_formula_sum            'Cl Na'\n_chemical_name_systematic        'Sodium chloride'\n_space_group_IT_number           225\n_symmetry_cell_setting           cubic\n_symmetry_Int_Tables_number      225\n_symmetry_space_group_name_Hall  '-F 4 2 3'\n_symmetry_space_group_name_H-M   'F m -3 m'\n_cell_angle_alpha                90\n_cell_angle_beta                 90\n_cell_angle_gamma                90\n_cell_formula_units_Z            4\n_cell_length_a                   5.62\n_cell_length_b                   5.62\n_cell_length_c                   5.62\n_cell_volume                     177.5\n_refine_ls_R_factor_all          0.022\n_cod_database_code               1000041\nloop_\n_symmetry_equiv_pos_as_xyz\nx,y,z\ny,z,x\nz,x,y\nx,z,y\ny,x,z\nz,y,x\nx,-y,-z\ny,-z,-x\nz,-x,-y\nx,-z,-y\ny,-x,-z\nz,-y,-x\n-x,y,-z\n-y,z,-x\n-z,x,-y\n-x,z,-y\n-y,x,-z\n-z,y,-x\n-x,-y,z\n-y,-z,x\n-z,-x,y\n-x,-z,y\n-y,-x,z\n-z,-y,x\n-x,-y,-z\n-y,-z,-x\n-z,-x,-y\n-x,-z,-y\n-y,-x,-z\n-z,-y,-x\n-x,y,z\n-y,z,x\n-z,x,y\n-x,z,y\n-y,x,z\n-z,y,x\nx,-y,z\ny,-z,x\nz,-x,y\nx,-z,y\ny,-x,z\nz,-y,x\nx,y,-z\ny,z,-x\nz,x,-y\nx,z,-y\ny,x,-z\nz,y,-x\nx,1/2+y,1/2+z\n1/2+x,y,1/2+z\n1/2+x,1/2+y,z\ny,1/2+z,1/2+x\n1/2+y,z,1/2+x\n1/2+y,1/2+z,x\nz,1/2+x,1/2+y\n1/2+z,x,1/2+y\n1/2+z,1/2+x,y\nx,1/2+z,1/2+y\n1/2+x,z,1/2+y\n1/2+x,1/2+z,y\ny,1/2+x,1/2+z\n1/2+y,x,1/2+z\n1/2+y,1/2+x,z\nz,1/2+y,1/2+x\n1/2+z,y,1/2+x\n1/2+z,1/2+y,x\nx,1/2-y,1/2-z\n1/2+x,-y,1/2-z\n1/2+x,1/2-y,-z\ny,1/2-z,1/2-x\n1/2+y,-z,1/2-x\n1/2+y,1/2-z,-x\nz,1/2-x,1/2-y\n1/2+z,-x,1/2-y\n1/2+z,1/2-x,-y\nx,1/2-z,1/2-y\n1/2+x,-z,1/2-y\n1/2+x,1/2-z,-y\ny,1/2-x,1/2-z\n1/2+y,-x,1/2-z\n1/2+y,1/2-x,-z\nz,1/2-y,1/2-x\n1/2+z,-y,1/2-x\n1/2+z,1/2-y,-x\n-x,1/2+y,1/2-z\n1/2-x,y,1/2-z\n1/2-x,1/2+y,-z\n-y,1/2+z,1/2-x\n1/2-y,z,1/2-x\n1/2-y,1/2+z,-x\n-z,1/2+x,1/2-y\n1/2-z,x,1/2-y\n1/2-z,1/2+x,-y\n-x,1/2+z,1/2-y\n1/2-x,z,1/2-y\n1/2-x,1/2+z,-y\n-y,1/2+x,1/2-z\n1/2-y,x,1/2-z\n1/2-y,1/2+x,-z\n-z,1/2+y,1/2-x\n1/2-z,y,1/2-x\n1/2-z,1/2+y,-x\n-x,1/2-y,1/2+z\n1/2-x,-y,1/2+z\n1/2-x,1/2-y,z\n-y,1/2-z,1/2+x\n1/2-y,-z,1/2+x\n1/2-y,1/2-z,x\n-z,1/2-x,1/2+y\n1/2-z,-x,1/2+y\n1/2-z,1/2-x,y\n-x,1/2-z,1/2+y\n1/2-x,-z,1/2+y\n1/2-x,1/2-z,y\n-y,1/2-x,1/2+z\n1/2-y,-x,1/2+z\n1/2-y,1/2-x,z\n-z,1/2-y,1/2+x\n1/2-z,-y,1/2+x\n1/2-z,1/2-y,x\n-x,1/2-y,1/2-z\n1/2-x,-y,1/2-z\n1/2-x,1/2-y,-z\n-y,1/2-z,1/2-x\n1/2-y,-z,1/2-x\n1/2-y,1/2-z,-x\n-z,1/2-x,1/2-y\n1/2-z,-x,1/2-y\n1/2-z,1/2-x,-y\n-x,1/2-z,1/2-y\n1/2-x,-z,1/2-y\n1/2-x,1/2-z,-y\n-y,1/2-x,1/2-z\n1/2-y,-x,1/2-z\n1/2-y,1/2-x,-z\n-z,1/2-y,1/2-x\n1/2-z,-y,1/2-x\n1/2-z,1/2-y,-x\n-x,1/2+y,1/2+z\n1/2-x,y,1/2+z\n1/2-x,1/2+y,z\n-y,1/2+z,1/2+x\n1/2-y,z,1/2+x\n1/2-y,1/2+z,x\n-z,1/2+x,1/2+y\n1/2-z,x,1/2+y\n1/2-z,1/2+x,y\n-x,1/2+z,1/2+y\n1/2-x,z,1/2+y\n1/2-x,1/2+z,y\n-y,1/2+x,1/2+z\n1/2-y,x,1/2+z\n1/2-y,1/2+x,z\n-z,1/2+y,1/2+x\n1/2-z,y,1/2+x\n1/2-z,1/2+y,x\nx,1/2-y,1/2+z\n1/2+x,-y,1/2+z\n1/2+x,1/2-y,z\ny,1/2-z,1/2+x\n1/2+y,-z,1/2+x\n1/2+y,1/2-z,x\nz,1/2-x,1/2+y\n1/2+z,-x,1/2+y\n1/2+z,1/2-x,y\nx,1/2-z,1/2+y\n1/2+x,-z,1/2+y\n1/2+x,1/2-z,y\ny,1/2-x,1/2+z\n1/2+y,-x,1/2+z\n1/2+y,1/2-x,z\nz,1/2-y,1/2+x\n1/2+z,-y,1/2+x\n1/2+z,1/2-y,x\nx,1/2+y,1/2-z\n1/2+x,y,1/2-z\n1/2+x,1/2+y,-z\ny,1/2+z,1/2-x\n1/2+y,z,1/2-x\n1/2+y,1/2+z,-x\nz,1/2+x,1/2-y\n1/2+z,x,1/2-y\n1/2+z,1/2+x,-y\nx,1/2+z,1/2-y\n1/2+x,z,1/2-y\n1/2+x,1/2+z,-y\ny,1/2+x,1/2-z\n1/2+y,x,1/2-z\n1/2+y,1/2+x,-z\nz,1/2+y,1/2-x\n1/2+z,y,1/2-x\n1/2+z,1/2+y,-x\nloop_\n_atom_site_label\n_atom_site_type_symbol\n_atom_site_symmetry_multiplicity\n_atom_site_Wyckoff_symbol\n_atom_site_fract_x\n_atom_site_fract_y\n_atom_site_fract_z\n_atom_site_occupancy\n_atom_site_attached_hydrogens\n_atom_site_calc_flag\nNa1 Na1+ 4 a 0. 0. 0. 1. 0 d\nCl1 Cl1- 4 b 0.5 0.5 0.5 1. 0 d\nloop_\n_atom_type_symbol\n_atom_type_oxidation_number\nNa1+ 1.000\nCl1- -1.000\n",
                ]
            ],
            "subject_type": "CIF",
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)
tests.append(
    {
        "service_type": "get_crystal_property",
        "service_name": "get crystal bulk_moduli",
        "parameters": {
            "property_type": [
                "bulk_moduli",
            ],
            "algorithm_version": "v0",
            "subjects": [
                [
                    "1000041.cif",
                    "#------------------------------------------------------------------------------\n#$Date: 2015-01-27 21:58:39 +0200 (Tue, 27 Jan 2015) $\n#$Revision: 130149 $\n#$URL: svn://www.crystallography.net/cod/cif/1/00/00/1000041.cif $\n#------------------------------------------------------------------------------\n#\n# This file is available in the Crystallography Open Database (COD),\n# http://www.crystallography.net/\n#\n# All data on this site have been placed in the public domain by the\n# contributors.\n#\ndata_1000041\nloop_\n_publ_author_name\n'Abrahams, S C'\n'Bernstein, J L'\n_publ_section_title\n;\nAccuracy of an automatic diffractometer. measurement of the sodium\nchloride structure factors\n;\n_journal_coden_ASTM              ACCRA9\n_journal_name_full               'Acta Crystallographica (1,1948-23,1967)'\n_journal_page_first              926\n_journal_page_last               932\n_journal_paper_doi               10.1107/S0365110X65002244\n_journal_volume                  18\n_journal_year                    1965\n_chemical_formula_structural     'Na Cl'\n_chemical_formula_sum            'Cl Na'\n_chemical_name_systematic        'Sodium chloride'\n_space_group_IT_number           225\n_symmetry_cell_setting           cubic\n_symmetry_Int_Tables_number      225\n_symmetry_space_group_name_Hall  '-F 4 2 3'\n_symmetry_space_group_name_H-M   'F m -3 m'\n_cell_angle_alpha                90\n_cell_angle_beta                 90\n_cell_angle_gamma                90\n_cell_formula_units_Z            4\n_cell_length_a                   5.62\n_cell_length_b                   5.62\n_cell_length_c                   5.62\n_cell_volume                     177.5\n_refine_ls_R_factor_all          0.022\n_cod_database_code               1000041\nloop_\n_symmetry_equiv_pos_as_xyz\nx,y,z\ny,z,x\nz,x,y\nx,z,y\ny,x,z\nz,y,x\nx,-y,-z\ny,-z,-x\nz,-x,-y\nx,-z,-y\ny,-x,-z\nz,-y,-x\n-x,y,-z\n-y,z,-x\n-z,x,-y\n-x,z,-y\n-y,x,-z\n-z,y,-x\n-x,-y,z\n-y,-z,x\n-z,-x,y\n-x,-z,y\n-y,-x,z\n-z,-y,x\n-x,-y,-z\n-y,-z,-x\n-z,-x,-y\n-x,-z,-y\n-y,-x,-z\n-z,-y,-x\n-x,y,z\n-y,z,x\n-z,x,y\n-x,z,y\n-y,x,z\n-z,y,x\nx,-y,z\ny,-z,x\nz,-x,y\nx,-z,y\ny,-x,z\nz,-y,x\nx,y,-z\ny,z,-x\nz,x,-y\nx,z,-y\ny,x,-z\nz,y,-x\nx,1/2+y,1/2+z\n1/2+x,y,1/2+z\n1/2+x,1/2+y,z\ny,1/2+z,1/2+x\n1/2+y,z,1/2+x\n1/2+y,1/2+z,x\nz,1/2+x,1/2+y\n1/2+z,x,1/2+y\n1/2+z,1/2+x,y\nx,1/2+z,1/2+y\n1/2+x,z,1/2+y\n1/2+x,1/2+z,y\ny,1/2+x,1/2+z\n1/2+y,x,1/2+z\n1/2+y,1/2+x,z\nz,1/2+y,1/2+x\n1/2+z,y,1/2+x\n1/2+z,1/2+y,x\nx,1/2-y,1/2-z\n1/2+x,-y,1/2-z\n1/2+x,1/2-y,-z\ny,1/2-z,1/2-x\n1/2+y,-z,1/2-x\n1/2+y,1/2-z,-x\nz,1/2-x,1/2-y\n1/2+z,-x,1/2-y\n1/2+z,1/2-x,-y\nx,1/2-z,1/2-y\n1/2+x,-z,1/2-y\n1/2+x,1/2-z,-y\ny,1/2-x,1/2-z\n1/2+y,-x,1/2-z\n1/2+y,1/2-x,-z\nz,1/2-y,1/2-x\n1/2+z,-y,1/2-x\n1/2+z,1/2-y,-x\n-x,1/2+y,1/2-z\n1/2-x,y,1/2-z\n1/2-x,1/2+y,-z\n-y,1/2+z,1/2-x\n1/2-y,z,1/2-x\n1/2-y,1/2+z,-x\n-z,1/2+x,1/2-y\n1/2-z,x,1/2-y\n1/2-z,1/2+x,-y\n-x,1/2+z,1/2-y\n1/2-x,z,1/2-y\n1/2-x,1/2+z,-y\n-y,1/2+x,1/2-z\n1/2-y,x,1/2-z\n1/2-y,1/2+x,-z\n-z,1/2+y,1/2-x\n1/2-z,y,1/2-x\n1/2-z,1/2+y,-x\n-x,1/2-y,1/2+z\n1/2-x,-y,1/2+z\n1/2-x,1/2-y,z\n-y,1/2-z,1/2+x\n1/2-y,-z,1/2+x\n1/2-y,1/2-z,x\n-z,1/2-x,1/2+y\n1/2-z,-x,1/2+y\n1/2-z,1/2-x,y\n-x,1/2-z,1/2+y\n1/2-x,-z,1/2+y\n1/2-x,1/2-z,y\n-y,1/2-x,1/2+z\n1/2-y,-x,1/2+z\n1/2-y,1/2-x,z\n-z,1/2-y,1/2+x\n1/2-z,-y,1/2+x\n1/2-z,1/2-y,x\n-x,1/2-y,1/2-z\n1/2-x,-y,1/2-z\n1/2-x,1/2-y,-z\n-y,1/2-z,1/2-x\n1/2-y,-z,1/2-x\n1/2-y,1/2-z,-x\n-z,1/2-x,1/2-y\n1/2-z,-x,1/2-y\n1/2-z,1/2-x,-y\n-x,1/2-z,1/2-y\n1/2-x,-z,1/2-y\n1/2-x,1/2-z,-y\n-y,1/2-x,1/2-z\n1/2-y,-x,1/2-z\n1/2-y,1/2-x,-z\n-z,1/2-y,1/2-x\n1/2-z,-y,1/2-x\n1/2-z,1/2-y,-x\n-x,1/2+y,1/2+z\n1/2-x,y,1/2+z\n1/2-x,1/2+y,z\n-y,1/2+z,1/2+x\n1/2-y,z,1/2+x\n1/2-y,1/2+z,x\n-z,1/2+x,1/2+y\n1/2-z,x,1/2+y\n1/2-z,1/2+x,y\n-x,1/2+z,1/2+y\n1/2-x,z,1/2+y\n1/2-x,1/2+z,y\n-y,1/2+x,1/2+z\n1/2-y,x,1/2+z\n1/2-y,1/2+x,z\n-z,1/2+y,1/2+x\n1/2-z,y,1/2+x\n1/2-z,1/2+y,x\nx,1/2-y,1/2+z\n1/2+x,-y,1/2+z\n1/2+x,1/2-y,z\ny,1/2-z,1/2+x\n1/2+y,-z,1/2+x\n1/2+y,1/2-z,x\nz,1/2-x,1/2+y\n1/2+z,-x,1/2+y\n1/2+z,1/2-x,y\nx,1/2-z,1/2+y\n1/2+x,-z,1/2+y\n1/2+x,1/2-z,y\ny,1/2-x,1/2+z\n1/2+y,-x,1/2+z\n1/2+y,1/2-x,z\nz,1/2-y,1/2+x\n1/2+z,-y,1/2+x\n1/2+z,1/2-y,x\nx,1/2+y,1/2-z\n1/2+x,y,1/2-z\n1/2+x,1/2+y,-z\ny,1/2+z,1/2-x\n1/2+y,z,1/2-x\n1/2+y,1/2+z,-x\nz,1/2+x,1/2-y\n1/2+z,x,1/2-y\n1/2+z,1/2+x,-y\nx,1/2+z,1/2-y\n1/2+x,z,1/2-y\n1/2+x,1/2+z,-y\ny,1/2+x,1/2-z\n1/2+y,x,1/2-z\n1/2+y,1/2+x,-z\nz,1/2+y,1/2-x\n1/2+z,y,1/2-x\n1/2+z,1/2+y,-x\nloop_\n_atom_site_label\n_atom_site_type_symbol\n_atom_site_symmetry_multiplicity\n_atom_site_Wyckoff_symbol\n_atom_site_fract_x\n_atom_site_fract_y\n_atom_site_fract_z\n_atom_site_occupancy\n_atom_site_attached_hydrogens\n_atom_site_calc_flag\nNa1 Na1+ 4 a 0. 0. 0. 1. 0 d\nCl1 Cl1- 4 b 0.5 0.5 0.5 1. 0 d\nloop_\n_atom_type_symbol\n_atom_type_oxidation_number\nNa1+ 1.000\nCl1- -1.000\n",
                ]
            ],
            "subject_type": "CIF",
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)
tests.append(
    {
        "service_type": "get_crystal_property",
        "service_name": "get crystal shear_moduli",
        "parameters": {
            "property_type": [
                "shear_moduli",
            ],
            "algorithm_version": "v0",
            "subjects": [
                [
                    "1000041.cif",
                    "#------------------------------------------------------------------------------\n#$Date: 2015-01-27 21:58:39 +0200 (Tue, 27 Jan 2015) $\n#$Revision: 130149 $\n#$URL: svn://www.crystallography.net/cod/cif/1/00/00/1000041.cif $\n#------------------------------------------------------------------------------\n#\n# This file is available in the Crystallography Open Database (COD),\n# http://www.crystallography.net/\n#\n# All data on this site have been placed in the public domain by the\n# contributors.\n#\ndata_1000041\nloop_\n_publ_author_name\n'Abrahams, S C'\n'Bernstein, J L'\n_publ_section_title\n;\nAccuracy of an automatic diffractometer. measurement of the sodium\nchloride structure factors\n;\n_journal_coden_ASTM              ACCRA9\n_journal_name_full               'Acta Crystallographica (1,1948-23,1967)'\n_journal_page_first              926\n_journal_page_last               932\n_journal_paper_doi               10.1107/S0365110X65002244\n_journal_volume                  18\n_journal_year                    1965\n_chemical_formula_structural     'Na Cl'\n_chemical_formula_sum            'Cl Na'\n_chemical_name_systematic        'Sodium chloride'\n_space_group_IT_number           225\n_symmetry_cell_setting           cubic\n_symmetry_Int_Tables_number      225\n_symmetry_space_group_name_Hall  '-F 4 2 3'\n_symmetry_space_group_name_H-M   'F m -3 m'\n_cell_angle_alpha                90\n_cell_angle_beta                 90\n_cell_angle_gamma                90\n_cell_formula_units_Z            4\n_cell_length_a                   5.62\n_cell_length_b                   5.62\n_cell_length_c                   5.62\n_cell_volume                     177.5\n_refine_ls_R_factor_all          0.022\n_cod_database_code               1000041\nloop_\n_symmetry_equiv_pos_as_xyz\nx,y,z\ny,z,x\nz,x,y\nx,z,y\ny,x,z\nz,y,x\nx,-y,-z\ny,-z,-x\nz,-x,-y\nx,-z,-y\ny,-x,-z\nz,-y,-x\n-x,y,-z\n-y,z,-x\n-z,x,-y\n-x,z,-y\n-y,x,-z\n-z,y,-x\n-x,-y,z\n-y,-z,x\n-z,-x,y\n-x,-z,y\n-y,-x,z\n-z,-y,x\n-x,-y,-z\n-y,-z,-x\n-z,-x,-y\n-x,-z,-y\n-y,-x,-z\n-z,-y,-x\n-x,y,z\n-y,z,x\n-z,x,y\n-x,z,y\n-y,x,z\n-z,y,x\nx,-y,z\ny,-z,x\nz,-x,y\nx,-z,y\ny,-x,z\nz,-y,x\nx,y,-z\ny,z,-x\nz,x,-y\nx,z,-y\ny,x,-z\nz,y,-x\nx,1/2+y,1/2+z\n1/2+x,y,1/2+z\n1/2+x,1/2+y,z\ny,1/2+z,1/2+x\n1/2+y,z,1/2+x\n1/2+y,1/2+z,x\nz,1/2+x,1/2+y\n1/2+z,x,1/2+y\n1/2+z,1/2+x,y\nx,1/2+z,1/2+y\n1/2+x,z,1/2+y\n1/2+x,1/2+z,y\ny,1/2+x,1/2+z\n1/2+y,x,1/2+z\n1/2+y,1/2+x,z\nz,1/2+y,1/2+x\n1/2+z,y,1/2+x\n1/2+z,1/2+y,x\nx,1/2-y,1/2-z\n1/2+x,-y,1/2-z\n1/2+x,1/2-y,-z\ny,1/2-z,1/2-x\n1/2+y,-z,1/2-x\n1/2+y,1/2-z,-x\nz,1/2-x,1/2-y\n1/2+z,-x,1/2-y\n1/2+z,1/2-x,-y\nx,1/2-z,1/2-y\n1/2+x,-z,1/2-y\n1/2+x,1/2-z,-y\ny,1/2-x,1/2-z\n1/2+y,-x,1/2-z\n1/2+y,1/2-x,-z\nz,1/2-y,1/2-x\n1/2+z,-y,1/2-x\n1/2+z,1/2-y,-x\n-x,1/2+y,1/2-z\n1/2-x,y,1/2-z\n1/2-x,1/2+y,-z\n-y,1/2+z,1/2-x\n1/2-y,z,1/2-x\n1/2-y,1/2+z,-x\n-z,1/2+x,1/2-y\n1/2-z,x,1/2-y\n1/2-z,1/2+x,-y\n-x,1/2+z,1/2-y\n1/2-x,z,1/2-y\n1/2-x,1/2+z,-y\n-y,1/2+x,1/2-z\n1/2-y,x,1/2-z\n1/2-y,1/2+x,-z\n-z,1/2+y,1/2-x\n1/2-z,y,1/2-x\n1/2-z,1/2+y,-x\n-x,1/2-y,1/2+z\n1/2-x,-y,1/2+z\n1/2-x,1/2-y,z\n-y,1/2-z,1/2+x\n1/2-y,-z,1/2+x\n1/2-y,1/2-z,x\n-z,1/2-x,1/2+y\n1/2-z,-x,1/2+y\n1/2-z,1/2-x,y\n-x,1/2-z,1/2+y\n1/2-x,-z,1/2+y\n1/2-x,1/2-z,y\n-y,1/2-x,1/2+z\n1/2-y,-x,1/2+z\n1/2-y,1/2-x,z\n-z,1/2-y,1/2+x\n1/2-z,-y,1/2+x\n1/2-z,1/2-y,x\n-x,1/2-y,1/2-z\n1/2-x,-y,1/2-z\n1/2-x,1/2-y,-z\n-y,1/2-z,1/2-x\n1/2-y,-z,1/2-x\n1/2-y,1/2-z,-x\n-z,1/2-x,1/2-y\n1/2-z,-x,1/2-y\n1/2-z,1/2-x,-y\n-x,1/2-z,1/2-y\n1/2-x,-z,1/2-y\n1/2-x,1/2-z,-y\n-y,1/2-x,1/2-z\n1/2-y,-x,1/2-z\n1/2-y,1/2-x,-z\n-z,1/2-y,1/2-x\n1/2-z,-y,1/2-x\n1/2-z,1/2-y,-x\n-x,1/2+y,1/2+z\n1/2-x,y,1/2+z\n1/2-x,1/2+y,z\n-y,1/2+z,1/2+x\n1/2-y,z,1/2+x\n1/2-y,1/2+z,x\n-z,1/2+x,1/2+y\n1/2-z,x,1/2+y\n1/2-z,1/2+x,y\n-x,1/2+z,1/2+y\n1/2-x,z,1/2+y\n1/2-x,1/2+z,y\n-y,1/2+x,1/2+z\n1/2-y,x,1/2+z\n1/2-y,1/2+x,z\n-z,1/2+y,1/2+x\n1/2-z,y,1/2+x\n1/2-z,1/2+y,x\nx,1/2-y,1/2+z\n1/2+x,-y,1/2+z\n1/2+x,1/2-y,z\ny,1/2-z,1/2+x\n1/2+y,-z,1/2+x\n1/2+y,1/2-z,x\nz,1/2-x,1/2+y\n1/2+z,-x,1/2+y\n1/2+z,1/2-x,y\nx,1/2-z,1/2+y\n1/2+x,-z,1/2+y\n1/2+x,1/2-z,y\ny,1/2-x,1/2+z\n1/2+y,-x,1/2+z\n1/2+y,1/2-x,z\nz,1/2-y,1/2+x\n1/2+z,-y,1/2+x\n1/2+z,1/2-y,x\nx,1/2+y,1/2-z\n1/2+x,y,1/2-z\n1/2+x,1/2+y,-z\ny,1/2+z,1/2-x\n1/2+y,z,1/2-x\n1/2+y,1/2+z,-x\nz,1/2+x,1/2-y\n1/2+z,x,1/2-y\n1/2+z,1/2+x,-y\nx,1/2+z,1/2-y\n1/2+x,z,1/2-y\n1/2+x,1/2+z,-y\ny,1/2+x,1/2-z\n1/2+y,x,1/2-z\n1/2+y,1/2+x,-z\nz,1/2+y,1/2-x\n1/2+z,y,1/2-x\n1/2+z,1/2+y,-x\nloop_\n_atom_site_label\n_atom_site_type_symbol\n_atom_site_symmetry_multiplicity\n_atom_site_Wyckoff_symbol\n_atom_site_fract_x\n_atom_site_fract_y\n_atom_site_fract_z\n_atom_site_occupancy\n_atom_site_attached_hydrogens\n_atom_site_calc_flag\nNa1 Na1+ 4 a 0. 0. 0. 1. 0 d\nCl1 Cl1- 4 b 0.5 0.5 0.5 1. 0 d\nloop_\n_atom_type_symbol\n_atom_type_oxidation_number\nNa1+ 1.000\nCl1- -1.000\n",
                ]
            ],
            "subject_type": "CIF",
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)
tests.append(
    {
        "service_type": "get_crystal_property",
        "service_name": "get crystal poisson_ratio",
        "parameters": {
            "property_type": [
                "poisson_ratio",
            ],
            "algorithm_version": "v0",
            "subjects": [
                [
                    "1000041.cif",
                    "#------------------------------------------------------------------------------\n#$Date: 2015-01-27 21:58:39 +0200 (Tue, 27 Jan 2015) $\n#$Revision: 130149 $\n#$URL: svn://www.crystallography.net/cod/cif/1/00/00/1000041.cif $\n#------------------------------------------------------------------------------\n#\n# This file is available in the Crystallography Open Database (COD),\n# http://www.crystallography.net/\n#\n# All data on this site have been placed in the public domain by the\n# contributors.\n#\ndata_1000041\nloop_\n_publ_author_name\n'Abrahams, S C'\n'Bernstein, J L'\n_publ_section_title\n;\nAccuracy of an automatic diffractometer. measurement of the sodium\nchloride structure factors\n;\n_journal_coden_ASTM              ACCRA9\n_journal_name_full               'Acta Crystallographica (1,1948-23,1967)'\n_journal_page_first              926\n_journal_page_last               932\n_journal_paper_doi               10.1107/S0365110X65002244\n_journal_volume                  18\n_journal_year                    1965\n_chemical_formula_structural     'Na Cl'\n_chemical_formula_sum            'Cl Na'\n_chemical_name_systematic        'Sodium chloride'\n_space_group_IT_number           225\n_symmetry_cell_setting           cubic\n_symmetry_Int_Tables_number      225\n_symmetry_space_group_name_Hall  '-F 4 2 3'\n_symmetry_space_group_name_H-M   'F m -3 m'\n_cell_angle_alpha                90\n_cell_angle_beta                 90\n_cell_angle_gamma                90\n_cell_formula_units_Z            4\n_cell_length_a                   5.62\n_cell_length_b                   5.62\n_cell_length_c                   5.62\n_cell_volume                     177.5\n_refine_ls_R_factor_all          0.022\n_cod_database_code               1000041\nloop_\n_symmetry_equiv_pos_as_xyz\nx,y,z\ny,z,x\nz,x,y\nx,z,y\ny,x,z\nz,y,x\nx,-y,-z\ny,-z,-x\nz,-x,-y\nx,-z,-y\ny,-x,-z\nz,-y,-x\n-x,y,-z\n-y,z,-x\n-z,x,-y\n-x,z,-y\n-y,x,-z\n-z,y,-x\n-x,-y,z\n-y,-z,x\n-z,-x,y\n-x,-z,y\n-y,-x,z\n-z,-y,x\n-x,-y,-z\n-y,-z,-x\n-z,-x,-y\n-x,-z,-y\n-y,-x,-z\n-z,-y,-x\n-x,y,z\n-y,z,x\n-z,x,y\n-x,z,y\n-y,x,z\n-z,y,x\nx,-y,z\ny,-z,x\nz,-x,y\nx,-z,y\ny,-x,z\nz,-y,x\nx,y,-z\ny,z,-x\nz,x,-y\nx,z,-y\ny,x,-z\nz,y,-x\nx,1/2+y,1/2+z\n1/2+x,y,1/2+z\n1/2+x,1/2+y,z\ny,1/2+z,1/2+x\n1/2+y,z,1/2+x\n1/2+y,1/2+z,x\nz,1/2+x,1/2+y\n1/2+z,x,1/2+y\n1/2+z,1/2+x,y\nx,1/2+z,1/2+y\n1/2+x,z,1/2+y\n1/2+x,1/2+z,y\ny,1/2+x,1/2+z\n1/2+y,x,1/2+z\n1/2+y,1/2+x,z\nz,1/2+y,1/2+x\n1/2+z,y,1/2+x\n1/2+z,1/2+y,x\nx,1/2-y,1/2-z\n1/2+x,-y,1/2-z\n1/2+x,1/2-y,-z\ny,1/2-z,1/2-x\n1/2+y,-z,1/2-x\n1/2+y,1/2-z,-x\nz,1/2-x,1/2-y\n1/2+z,-x,1/2-y\n1/2+z,1/2-x,-y\nx,1/2-z,1/2-y\n1/2+x,-z,1/2-y\n1/2+x,1/2-z,-y\ny,1/2-x,1/2-z\n1/2+y,-x,1/2-z\n1/2+y,1/2-x,-z\nz,1/2-y,1/2-x\n1/2+z,-y,1/2-x\n1/2+z,1/2-y,-x\n-x,1/2+y,1/2-z\n1/2-x,y,1/2-z\n1/2-x,1/2+y,-z\n-y,1/2+z,1/2-x\n1/2-y,z,1/2-x\n1/2-y,1/2+z,-x\n-z,1/2+x,1/2-y\n1/2-z,x,1/2-y\n1/2-z,1/2+x,-y\n-x,1/2+z,1/2-y\n1/2-x,z,1/2-y\n1/2-x,1/2+z,-y\n-y,1/2+x,1/2-z\n1/2-y,x,1/2-z\n1/2-y,1/2+x,-z\n-z,1/2+y,1/2-x\n1/2-z,y,1/2-x\n1/2-z,1/2+y,-x\n-x,1/2-y,1/2+z\n1/2-x,-y,1/2+z\n1/2-x,1/2-y,z\n-y,1/2-z,1/2+x\n1/2-y,-z,1/2+x\n1/2-y,1/2-z,x\n-z,1/2-x,1/2+y\n1/2-z,-x,1/2+y\n1/2-z,1/2-x,y\n-x,1/2-z,1/2+y\n1/2-x,-z,1/2+y\n1/2-x,1/2-z,y\n-y,1/2-x,1/2+z\n1/2-y,-x,1/2+z\n1/2-y,1/2-x,z\n-z,1/2-y,1/2+x\n1/2-z,-y,1/2+x\n1/2-z,1/2-y,x\n-x,1/2-y,1/2-z\n1/2-x,-y,1/2-z\n1/2-x,1/2-y,-z\n-y,1/2-z,1/2-x\n1/2-y,-z,1/2-x\n1/2-y,1/2-z,-x\n-z,1/2-x,1/2-y\n1/2-z,-x,1/2-y\n1/2-z,1/2-x,-y\n-x,1/2-z,1/2-y\n1/2-x,-z,1/2-y\n1/2-x,1/2-z,-y\n-y,1/2-x,1/2-z\n1/2-y,-x,1/2-z\n1/2-y,1/2-x,-z\n-z,1/2-y,1/2-x\n1/2-z,-y,1/2-x\n1/2-z,1/2-y,-x\n-x,1/2+y,1/2+z\n1/2-x,y,1/2+z\n1/2-x,1/2+y,z\n-y,1/2+z,1/2+x\n1/2-y,z,1/2+x\n1/2-y,1/2+z,x\n-z,1/2+x,1/2+y\n1/2-z,x,1/2+y\n1/2-z,1/2+x,y\n-x,1/2+z,1/2+y\n1/2-x,z,1/2+y\n1/2-x,1/2+z,y\n-y,1/2+x,1/2+z\n1/2-y,x,1/2+z\n1/2-y,1/2+x,z\n-z,1/2+y,1/2+x\n1/2-z,y,1/2+x\n1/2-z,1/2+y,x\nx,1/2-y,1/2+z\n1/2+x,-y,1/2+z\n1/2+x,1/2-y,z\ny,1/2-z,1/2+x\n1/2+y,-z,1/2+x\n1/2+y,1/2-z,x\nz,1/2-x,1/2+y\n1/2+z,-x,1/2+y\n1/2+z,1/2-x,y\nx,1/2-z,1/2+y\n1/2+x,-z,1/2+y\n1/2+x,1/2-z,y\ny,1/2-x,1/2+z\n1/2+y,-x,1/2+z\n1/2+y,1/2-x,z\nz,1/2-y,1/2+x\n1/2+z,-y,1/2+x\n1/2+z,1/2-y,x\nx,1/2+y,1/2-z\n1/2+x,y,1/2-z\n1/2+x,1/2+y,-z\ny,1/2+z,1/2-x\n1/2+y,z,1/2-x\n1/2+y,1/2+z,-x\nz,1/2+x,1/2-y\n1/2+z,x,1/2-y\n1/2+z,1/2+x,-y\nx,1/2+z,1/2-y\n1/2+x,z,1/2-y\n1/2+x,1/2+z,-y\ny,1/2+x,1/2-z\n1/2+y,x,1/2-z\n1/2+y,1/2+x,-z\nz,1/2+y,1/2-x\n1/2+z,y,1/2-x\n1/2+z,1/2+y,-x\nloop_\n_atom_site_label\n_atom_site_type_symbol\n_atom_site_symmetry_multiplicity\n_atom_site_Wyckoff_symbol\n_atom_site_fract_x\n_atom_site_fract_y\n_atom_site_fract_z\n_atom_site_occupancy\n_atom_site_attached_hydrogens\n_atom_site_calc_flag\nNa1 Na1+ 4 a 0. 0. 0. 1. 0 d\nCl1 Cl1- 4 b 0.5 0.5 0.5 1. 0 d\nloop_\n_atom_type_symbol\n_atom_type_oxidation_number\nNa1+ 1.000\nCl1- -1.000\n",
                ]
            ],
            "subject_type": "CIF",
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)

tests.append(
    {
        "service_type": "get_crystal_property",
        "service_name": "get crystal metal_semiconductor_classifier",
        "parameters": {
            "property_type": [
                "metal_semiconductor_classifier",
            ],
            "algorithm_version": "v0",
            "subjects": [
                [
                    "1000041.cif",
                    "#------------------------------------------------------------------------------\n#$Date: 2015-01-27 21:58:39 +0200 (Tue, 27 Jan 2015) $\n#$Revision: 130149 $\n#$URL: svn://www.crystallography.net/cod/cif/1/00/00/1000041.cif $\n#------------------------------------------------------------------------------\n#\n# This file is available in the Crystallography Open Database (COD),\n# http://www.crystallography.net/\n#\n# All data on this site have been placed in the public domain by the\n# contributors.\n#\ndata_1000041\nloop_\n_publ_author_name\n'Abrahams, S C'\n'Bernstein, J L'\n_publ_section_title\n;\nAccuracy of an automatic diffractometer. measurement of the sodium\nchloride structure factors\n;\n_journal_coden_ASTM              ACCRA9\n_journal_name_full               'Acta Crystallographica (1,1948-23,1967)'\n_journal_page_first              926\n_journal_page_last               932\n_journal_paper_doi               10.1107/S0365110X65002244\n_journal_volume                  18\n_journal_year                    1965\n_chemical_formula_structural     'Na Cl'\n_chemical_formula_sum            'Cl Na'\n_chemical_name_systematic        'Sodium chloride'\n_space_group_IT_number           225\n_symmetry_cell_setting           cubic\n_symmetry_Int_Tables_number      225\n_symmetry_space_group_name_Hall  '-F 4 2 3'\n_symmetry_space_group_name_H-M   'F m -3 m'\n_cell_angle_alpha                90\n_cell_angle_beta                 90\n_cell_angle_gamma                90\n_cell_formula_units_Z            4\n_cell_length_a                   5.62\n_cell_length_b                   5.62\n_cell_length_c                   5.62\n_cell_volume                     177.5\n_refine_ls_R_factor_all          0.022\n_cod_database_code               1000041\nloop_\n_symmetry_equiv_pos_as_xyz\nx,y,z\ny,z,x\nz,x,y\nx,z,y\ny,x,z\nz,y,x\nx,-y,-z\ny,-z,-x\nz,-x,-y\nx,-z,-y\ny,-x,-z\nz,-y,-x\n-x,y,-z\n-y,z,-x\n-z,x,-y\n-x,z,-y\n-y,x,-z\n-z,y,-x\n-x,-y,z\n-y,-z,x\n-z,-x,y\n-x,-z,y\n-y,-x,z\n-z,-y,x\n-x,-y,-z\n-y,-z,-x\n-z,-x,-y\n-x,-z,-y\n-y,-x,-z\n-z,-y,-x\n-x,y,z\n-y,z,x\n-z,x,y\n-x,z,y\n-y,x,z\n-z,y,x\nx,-y,z\ny,-z,x\nz,-x,y\nx,-z,y\ny,-x,z\nz,-y,x\nx,y,-z\ny,z,-x\nz,x,-y\nx,z,-y\ny,x,-z\nz,y,-x\nx,1/2+y,1/2+z\n1/2+x,y,1/2+z\n1/2+x,1/2+y,z\ny,1/2+z,1/2+x\n1/2+y,z,1/2+x\n1/2+y,1/2+z,x\nz,1/2+x,1/2+y\n1/2+z,x,1/2+y\n1/2+z,1/2+x,y\nx,1/2+z,1/2+y\n1/2+x,z,1/2+y\n1/2+x,1/2+z,y\ny,1/2+x,1/2+z\n1/2+y,x,1/2+z\n1/2+y,1/2+x,z\nz,1/2+y,1/2+x\n1/2+z,y,1/2+x\n1/2+z,1/2+y,x\nx,1/2-y,1/2-z\n1/2+x,-y,1/2-z\n1/2+x,1/2-y,-z\ny,1/2-z,1/2-x\n1/2+y,-z,1/2-x\n1/2+y,1/2-z,-x\nz,1/2-x,1/2-y\n1/2+z,-x,1/2-y\n1/2+z,1/2-x,-y\nx,1/2-z,1/2-y\n1/2+x,-z,1/2-y\n1/2+x,1/2-z,-y\ny,1/2-x,1/2-z\n1/2+y,-x,1/2-z\n1/2+y,1/2-x,-z\nz,1/2-y,1/2-x\n1/2+z,-y,1/2-x\n1/2+z,1/2-y,-x\n-x,1/2+y,1/2-z\n1/2-x,y,1/2-z\n1/2-x,1/2+y,-z\n-y,1/2+z,1/2-x\n1/2-y,z,1/2-x\n1/2-y,1/2+z,-x\n-z,1/2+x,1/2-y\n1/2-z,x,1/2-y\n1/2-z,1/2+x,-y\n-x,1/2+z,1/2-y\n1/2-x,z,1/2-y\n1/2-x,1/2+z,-y\n-y,1/2+x,1/2-z\n1/2-y,x,1/2-z\n1/2-y,1/2+x,-z\n-z,1/2+y,1/2-x\n1/2-z,y,1/2-x\n1/2-z,1/2+y,-x\n-x,1/2-y,1/2+z\n1/2-x,-y,1/2+z\n1/2-x,1/2-y,z\n-y,1/2-z,1/2+x\n1/2-y,-z,1/2+x\n1/2-y,1/2-z,x\n-z,1/2-x,1/2+y\n1/2-z,-x,1/2+y\n1/2-z,1/2-x,y\n-x,1/2-z,1/2+y\n1/2-x,-z,1/2+y\n1/2-x,1/2-z,y\n-y,1/2-x,1/2+z\n1/2-y,-x,1/2+z\n1/2-y,1/2-x,z\n-z,1/2-y,1/2+x\n1/2-z,-y,1/2+x\n1/2-z,1/2-y,x\n-x,1/2-y,1/2-z\n1/2-x,-y,1/2-z\n1/2-x,1/2-y,-z\n-y,1/2-z,1/2-x\n1/2-y,-z,1/2-x\n1/2-y,1/2-z,-x\n-z,1/2-x,1/2-y\n1/2-z,-x,1/2-y\n1/2-z,1/2-x,-y\n-x,1/2-z,1/2-y\n1/2-x,-z,1/2-y\n1/2-x,1/2-z,-y\n-y,1/2-x,1/2-z\n1/2-y,-x,1/2-z\n1/2-y,1/2-x,-z\n-z,1/2-y,1/2-x\n1/2-z,-y,1/2-x\n1/2-z,1/2-y,-x\n-x,1/2+y,1/2+z\n1/2-x,y,1/2+z\n1/2-x,1/2+y,z\n-y,1/2+z,1/2+x\n1/2-y,z,1/2+x\n1/2-y,1/2+z,x\n-z,1/2+x,1/2+y\n1/2-z,x,1/2+y\n1/2-z,1/2+x,y\n-x,1/2+z,1/2+y\n1/2-x,z,1/2+y\n1/2-x,1/2+z,y\n-y,1/2+x,1/2+z\n1/2-y,x,1/2+z\n1/2-y,1/2+x,z\n-z,1/2+y,1/2+x\n1/2-z,y,1/2+x\n1/2-z,1/2+y,x\nx,1/2-y,1/2+z\n1/2+x,-y,1/2+z\n1/2+x,1/2-y,z\ny,1/2-z,1/2+x\n1/2+y,-z,1/2+x\n1/2+y,1/2-z,x\nz,1/2-x,1/2+y\n1/2+z,-x,1/2+y\n1/2+z,1/2-x,y\nx,1/2-z,1/2+y\n1/2+x,-z,1/2+y\n1/2+x,1/2-z,y\ny,1/2-x,1/2+z\n1/2+y,-x,1/2+z\n1/2+y,1/2-x,z\nz,1/2-y,1/2+x\n1/2+z,-y,1/2+x\n1/2+z,1/2-y,x\nx,1/2+y,1/2-z\n1/2+x,y,1/2-z\n1/2+x,1/2+y,-z\ny,1/2+z,1/2-x\n1/2+y,z,1/2-x\n1/2+y,1/2+z,-x\nz,1/2+x,1/2-y\n1/2+z,x,1/2-y\n1/2+z,1/2+x,-y\nx,1/2+z,1/2-y\n1/2+x,z,1/2-y\n1/2+x,1/2+z,-y\ny,1/2+x,1/2-z\n1/2+y,x,1/2-z\n1/2+y,1/2+x,-z\nz,1/2+y,1/2-x\n1/2+z,y,1/2-x\n1/2+z,1/2+y,-x\nloop_\n_atom_site_label\n_atom_site_type_symbol\n_atom_site_symmetry_multiplicity\n_atom_site_Wyckoff_symbol\n_atom_site_fract_x\n_atom_site_fract_y\n_atom_site_fract_z\n_atom_site_occupancy\n_atom_site_attached_hydrogens\n_atom_site_calc_flag\nNa1 Na1+ 4 a 0. 0. 0. 1. 0 d\nCl1 Cl1- 4 b 0.5 0.5 0.5 1. 0 d\nloop_\n_atom_type_symbol\n_atom_type_oxidation_number\nNa1+ 1.000\nCl1- -1.000\n",
                ]
            ],
            "subject_type": "CIF",
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)

tests.append(
    {
        "service_type": "get_crystal_property",
        "service_name": "get crystal metal_nonmetal_classifier",
        "parameters": {
            "property_type": [
                "metal_nonmetal_classifier",
            ],
            "algorithm_version": "v0",
            "subjects": [
                [
                    "crf_data.csv",
                    "AgHgHW6,cubic\nAlGaH6Os,cubic\nBaAlTlH6,cubic\nBaCaH6Ir,cubic\nBaCaH6Rh,cubic\nBaCaHfSi6,cubic\nBaCrH6Ru,cubic\nBaMgZnH6,cubic\nBaMnVH6,cubic\n",
                ],
            ],
            "subject_type": "CIF",
        },
        "api_key": "api-dthgwrhrthrtrth",
    }
)
