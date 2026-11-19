 Loading weights: 100% 290/290 [00:00<00:00, 682.68it/s]=== BASE MODEL === Valid JSON: 48/50 (96%) | Exact Match: 0/50 (0%)
trainable params: 540,672 || all params: 494,573,440 || trainable%: 0.1093
Map: 100% 250/250 [00:00<00:00, 4622.21 examples/s]/usr/local/lib/python3.13/dist-packages/torch/_dynamo/eval_frame.py:1548: UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
  return fn(*args, **kwargs)

    
      
      
      [48/48 00:14, Epoch 3/3]
    
    
  
 
      Step
      Training Loss
    
  
  
    
      15
      2.612603
    
    
      30
      1.703332
    
    
      45
      1.246874
    
  
=== FINE-TUNED MODEL === Valid JSON: 50/50 (100%) | Exact Match: 18/50 (36%)
Sample Failures: [('Refund not received after 10 days (ticket #1251)', '{"category": "billing", "priority": "medium"}', '{"category": "issue", "priority": "high"}'), ('Need an invoice copy for last month (ticket #1252)', '{"category": "billing", "priority": "low"}', '{"category": "invoice", "priority": "low"}'), ('Unable to update my registered email address (ticket #1253)', '{"category": "account", "priority": "medium"}', '{"category": "issue", "priority": "high"}')]
Loading weights: 100% 290/290 [00:00<00:00, 705.86it/s]=== BASE MODEL === Valid JSON: 48/50 (96%) | Exact Match: 0/50 (0%)
trainable params: 540,672 || all params: 494,573,440 || trainable%: 0.1093
Map: 100% 250/250 [00:00<00:00, 4527.30 examples/s]/usr/local/lib/python3.13/dist-packages/torch/_dynamo/eval_frame.py:1548: UserWarning: torch.utils.checkpoint: the use_reentrant parameter should be passed explicitly. Starting in PyTorch 2.9, calling checkpoint without use_reentrant will raise an exception. use_reentrant=False is recommended, but if you need to preserve the current default behavior, you can pass use_reentrant=True. Refer to docs for more details on the differences between the two variants.
  return fn(*args, **kwargs)

    
      
      
      [48/48 00:14, Epoch 3/3]
    
    
  
 
      Step
      Training Loss
    
  
  
    
      15
      2.612603
    
    
      30
      1.703332
    
    
      45
      1.246874
    
  
=== FINE-TUNED MODEL === Valid JSON: 50/50 (100%) | Exact Match: 18/50 (36%)
Sample Failures: [('Refund not received after 10 days (ticket #1251)', '{"category": "billing", "priority": "medium"}', '{"category": "issue", "priority": "high"}'), ('Need an invoice copy for last month (ticket #1252)', '{"category": "billing", "priority": "low"}', '{"category": "invoice", "priority": "low"}'), ('Unable to update my registered email address (ticket #1253)', '{"category": "account", "priority": "medium"}', '{"category": "issue", "priority": "high"}')]
