export function getClerkError(err: unknown): string {
  if (
    err &&
    typeof err === "object" &&
    "errors" in err &&
    Array.isArray((err as Record<string, unknown>).errors)
  ) {
    const errors = (err as { errors: Array<{ longMessage?: string; message?: string }> }).errors
    if (errors.length > 0) {
      return errors[0].longMessage || errors[0].message || "An error occurred."
    }
  }
  return "Something went wrong. Please try again."
}
