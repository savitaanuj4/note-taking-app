from rest_framework.permissions import BasePermission

class IsOwnerOrSharedUser(BasePermission):
    message = "You do not have permission to access this object."

    def has_object_permission(self, request, view, obj):
        # Check if the user is the owner of the object
        if request.user == obj.creaed_by:
            return True

        # Check if the user is in the list of users the object is shared with
        shared_users = obj.shared_notes.values_list('shared_with', flat=True)
        if request.user.id in shared_users:
            return True

        return False