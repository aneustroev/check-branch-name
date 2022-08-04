check-branch-name
=========================

A check-branch-name hook for pre-commit.

See also: https://github.com/pre-commit/pre-commit


### Using with pre-commit

Add this to your `.pre-commit-config.yaml`

```yaml
-   repo: https://github.com/aneustroev/check-branch-name
    rev: v0.0.2  # Use the ref you want to point at
    hooks:
    -   id: add-msg-issue-prefix
        args:
            - --regexp=".*"
```
