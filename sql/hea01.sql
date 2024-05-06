INSERT INTO webapp_category (name) VALUES ('Health and Wellbeing');

INSERT INTO webapp_question (category_id, prompt, code) VALUES 
(1, 'Are there sufficient measures in place to ensure good indoor air quality?', 'Hea01');

INSERT INTO webapp_choice (question_id, text, score) VALUES 
((SELECT id FROM webapp_question WHERE code = 'Hea01'), 'Question not answered', 0),
((SELECT id FROM webapp_question WHERE code = 'Hea01'), 'No', 0),
((SELECT id FROM webapp_question WHERE code = 'Hea01'), 'Yes, ≥ 10% of the total area of the asset’s external walls and roof is glazed', 1),
((SELECT id FROM webapp_question WHERE code = 'Hea01'), 'Yes, ≥ 50% of occupied space meets the minimum performance requirements for glazed area as a percentage of floor area', 2),
((SELECT id FROM webapp_question WHERE code = 'Hea01'), 'Yes, ≥ 80% of occupied space meets the minimum performance requirements for glazed area as a percentage of floor area', 4),
((SELECT id FROM webapp_question WHERE code = 'Hea01'), 'Yes, all occupied space meets the minimum performance requirements for glazed area as a percentage of floor area', 5);

INSERT INTO webapp_question (category_id, prompt, code) VALUES 
(1, 'Are features that control glare from sunlight provided in relevant occupied space?', 'Hea02');

INSERT INTO webapp_choice (question_id, text, score) VALUES 
((SELECT id FROM webapp_question WHERE code = 'Hea02'), 'Question not answered', 0),
((SELECT id FROM webapp_question WHERE code = 'Hea02'), 'No', 0),
((SELECT id FROM webapp_question WHERE code = 'Hea02'), 'Yes, in ≥ 50% of all relevant occupied space', 2),
((SELECT id FROM webapp_question WHERE code = 'Hea02'), 'Yes, in ≥ 80% of all relevant occupied space', 4);