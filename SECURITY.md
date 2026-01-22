# 🔒 Security Policy

## Supported Versions

This project uses the following versions with security updates:

| Package | Version | Status |
|---------|---------|--------|
| Django | 4.2.26 | ✅ LTS with latest security patches |
| Pillow | 10.3.0 | ✅ Latest stable with security fixes |
| python-decouple | 3.8 | ✅ Stable |
| requests | 2.31.0 | ✅ Stable |

## Security Updates Applied

### Django 4.2.26 (Updated from 4.2.9)

The following vulnerabilities were fixed by updating to Django 4.2.26:

1. **SQL Injection in Column Aliases**
   - CVE: Multiple
   - Severity: High
   - Fixed in: 4.2.25+

2. **SQL Injection in HasKey(lhs, rhs) on Oracle**
   - CVE: Multiple
   - Severity: High
   - Fixed in: 4.2.17+

3. **SQL Injection via _connector Keyword**
   - CVE: Multiple
   - Severity: High
   - Fixed in: 4.2.26

4. **DoS in HttpResponseRedirect (Windows)**
   - CVE: Multiple
   - Severity: Medium
   - Fixed in: 4.2.26

5. **DoS in intcomma Template Filter**
   - CVE: Multiple
   - Severity: Medium
   - Fixed in: 4.2.10+

### Pillow 10.3.0 (Updated from 10.1.0)

1. **Buffer Overflow Vulnerability**
   - CVE: Multiple
   - Severity: High
   - Fixed in: 10.3.0

## Security Features Implemented

### Application Level

1. **CSRF Protection**
   - All forms include CSRF tokens
   - Django middleware enabled

2. **SQL Injection Protection**
   - Django ORM used throughout
   - No raw SQL queries
   - Parameterized queries

3. **XSS Protection**
   - Template auto-escaping enabled
   - User input sanitized
   - Content Security Policy ready

4. **Authentication & Authorization**
   - Admin area requires authentication
   - Django's built-in auth system
   - Password hashing (PBKDF2)

5. **Webhook Security**
   - Token-based authentication
   - Signature validation
   - HTTPS recommended

### Configuration

1. **Environment Variables**
   - Secrets in .env file
   - .env not committed to repo
   - .env.example provided

2. **Debug Mode**
   - DEBUG=False in production
   - Error pages don't leak info

3. **Allowed Hosts**
   - Configured per environment
   - Prevents host header attacks

## Reporting a Vulnerability

If you discover a security vulnerability, please:

1. **Do NOT** open a public issue
2. Email the maintainers privately
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

We will respond within 48 hours and work to fix the issue as quickly as possible.

## Security Best Practices for Deployment

### Required for Production

- [ ] Set `DEBUG=False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Use strong `SECRET_KEY`
- [ ] Enable HTTPS/SSL
- [ ] Configure secure cookies
- [ ] Set up proper firewall rules
- [ ] Regular dependency updates
- [ ] Database backups
- [ ] Monitor logs for suspicious activity

### Recommended

- [ ] Use environment-specific settings
- [ ] Implement rate limiting
- [ ] Set up security headers
- [ ] Enable Django security middleware
- [ ] Use Content Security Policy
- [ ] Implement logging and monitoring
- [ ] Regular security audits
- [ ] Keep dependencies updated

## Dependency Updates

Check for security updates regularly:

```bash
# Check for outdated packages
pip list --outdated

# Update specific package
pip install --upgrade Django

# Update all packages
pip install --upgrade -r requirements.txt
```

## Security Checklist

Before deploying to production, verify:

- [x] All dependencies are up-to-date
- [x] No known vulnerabilities in dependencies
- [x] DEBUG is False
- [x] SECRET_KEY is strong and unique
- [x] ALLOWED_HOSTS is configured
- [ ] HTTPS is enabled
- [ ] Secure cookies are configured
- [ ] Database credentials are secure
- [ ] Asaas API keys are in environment variables
- [ ] Webhook token is strong and secret

## Security Resources

- [Django Security Documentation](https://docs.djangoproject.com/en/stable/topics/security/)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security](https://python.readthedocs.io/en/latest/library/security_warnings.html)

## Updates

| Date | Version | Changes |
|------|---------|---------|
| 2026-01-22 | 1.0.0 | Initial release with Django 4.2.26 and Pillow 10.3.0 |

---

**Last Updated:** January 22, 2026
