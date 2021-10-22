---
# Generate Wowchemy CMS
type: wowchemycms
outputs:
- wowchemycms_config
- HTML
---
# Invitation: 
{{ .SiteURL }}/some/path/#invite_token={{ .Token }}

# Confirmation:
{{ .SiteURL }}/some/path/#confirmation_token={{ .Token }}

# Password recovery: 
{{ .SiteURL }}/some/path/#recovery_token={{ .Token }}
    
# Email change:
{{ .SiteURL }}/some/path/#email_change_token={{ .Token }}
