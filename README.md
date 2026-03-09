1. src/usdm_to_linkml/__init__.py - Package init exposing USDMToLinkMLConverter                                                                                                                          
  2. src/usdm_to_linkml/converter.py - Main converter module with:                                                                                                                                         
    - USDMToLinkMLConverter class that:                                                                                                                                                                    
        - Discovers all 97 USDM Pydantic models from usdm_model package                                                                                                                                    
      - Maps Python types to LinkML ranges (string, integer, float, boolean)                                                                                                                               
      - Preserves inheritance hierarchy via is_a                                                                                                                                                           
      - Marks base classes as abstract: true                                                                                                                                                               
      - Handles instanceType with designates_type: true and per-class slot_usage with equals_string                                                                                                        
      - Detects ID reference fields (*Id, *Ids) and sets inlined: false with inferred target class ranges                                                                                                  
      - Handles List[X] → multivalued: true                                                                                                                                                                
      - Handles Union[X, None] → required: false                                                                                                                                                           
  3. scripts/generate_schema.py - CLI entry point to generate the schema                                                                                                                                   
  4. output/usdm.yaml - Generated LinkML schema with:                                                                                                                                                      
    - 97 classes (72 USDM models + base classes + additional referenced classes)                                                                                                                           
    - 240 slots                                                                                                                                                                                            
    - Proper inheritance chains                                                                                                                                                                            
    - instanceType constraints per class                                                                                                                                                                   
  5. tests/test_converter.py - 26 tests covering:                                                                                                                                                          
    - Model discovery                                                                                                                                                                                      
    - Schema structure                                                                                                                                                                                     
    - Inheritance mapping                                                                                                                                                                                  
    - instanceType handling                                                                                                                                                                                
    - ID reference detection                                                                                                                                                                               
    - Type mapping                                                                                                                                                                                         
    - Schema validation with LinkML                                                                                                                                                                        
                                                                                                                                                                                                           
  Usage                                                                                                                                                                                                    
                                                                                                                                                                                                           
  # Activate virtual environment                                                                                                                                                                           
  source .venv/bin/activate                                                                                                                                                                                
                                                                                                                                                                                                           
  # Generate the schema                                                                                                                                                                                    
  python scripts/generate_schema.py                                                                                                                                                                        
                                                                                                                                                                                                           
  # Run tests                                                                                                                                                                                              
  pytest tests/test_converter.py -v                                                                                                                                                                        
                                                                                                                                                                                                           
  # Validate with LinkML                                                                                                                                                                                   
  linkml-lint output/usdm.yaml    
