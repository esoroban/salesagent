# Client Profile Fields

This document outlines all the fields that the outbound sales agent may collect during the conversation with a potential client.

---

## 1. Personal and Contact Information

- **name**  
  The name of the respondent (adult).  
  *Used in:* `record_basic_info`, `schedule_callback`

- **phone**  
  The respondent’s phone number.  
  *Used in:* `schedule_callback`

- **city**  
  The city where the client is located.  
  *Used in:* `record_basic_info`, `get_price`, `sign_for_promo`

---

## 2. Child Information

- **child_name**  
  The name of the child interested in the course.  
  *Used in:* `record_child_name`, `sign_for_promo`

---

## 3. Engagement Context

- **format**  
  The preferred format of the course: "онлайн" or "офлайн".  
  *Used in:* `record_basic_info`, `get_price`, `sign_for_promo`

- **time**  
  The preferred time for a callback, if the client is not ready to proceed immediately.  
  *Used in:* `schedule_callback`

- **interest_level**  
  The respondent's level of interest: `"high"`, `"medium"`, or `"low"`.  
  *Used in:* `log_interest_level`

- **objection_text**  
  Any concern or objection raised during the conversation.  
  *Used in:* `record_objection`

- **dialogue_stop_reason**  
  The reason for ending the conversation.  
  *Used in:* `stop_dialogue`
